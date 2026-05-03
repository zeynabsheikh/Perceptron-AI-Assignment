<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Agent: Wumpus Logic Engine</title>
    <style>
        :root { --bg: #f1f5f9; --primary: #1d4ed8; --accent: #38bdf8; --safe: #10b981; --danger: #ef4444; }
        body { font-family: 'Segoe UI', sans-serif; background: var(--bg); margin: 0; padding: 10px; color: #1e293b; overflow-x: hidden; }
        
        /* Main Layout for LinkedIn Video */
        .wrapper { max-width: 1000px; margin: 0 auto; display: flex; gap: 15px; align-items: flex-start; scale: 0.9; transform-origin: top; }
        
        .main-content { flex: 1.2; background: white; padding: 20px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        h2 { margin: 0 0 15px 0; font-size: 1.5rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
        
        .controls { display: flex; gap: 10px; margin-bottom: 15px; align-items: center; }
        input { width: 50px; padding: 8px; border: 2px solid #e2e8f0; border-radius: 6px; font-weight: bold; }
        button { padding: 8px 15px; border: none; border-radius: 6px; cursor: pointer; font-weight: 700; font-size: 0.9rem; }
        .btn-new { background: #334155; color: white; }
        .btn-exec { background: var(--safe); color: white; flex-grow: 1; }

        /* Smaller Grid for Video Fit */
        #grid { display: grid; gap: 8px; background: #f8fafc; padding: 10px; border-radius: 10px; border: 2px solid #e2e8f0; max-width: 500px; margin: 0 auto; }
        .cell { aspect-ratio: 1; background: #e2e8f0; border-radius: 6px; display: flex; align-items: center; justify-content: center; position: relative; font-size: 1.2rem; }
        .cell.visited { background: #ffffff; border: 1px solid #cbd5e1; }
        .cell.safe-border { border: 3px solid var(--safe); }
        .agent { width: 65%; height: 65%; background: #f59e0b; border-radius: 50%; box-shadow: 0 0 15px #f59e0b; border: 2px solid white; z-index: 2; }
        .hazard { background: #fee2e2 !important; border: 1px solid var(--danger) !important; }

        /* Compact Dashboard */
        .sidebar { width: 300px; background: #0f172a; color: white; padding: 20px; border-radius: 12px; }
        .stat-card { background: #1e293b; padding: 12px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid var(--accent); }
        .stat-label { font-size: 0.7rem; text-transform: uppercase; color: #94a3b8; }
        .stat-val { font-size: 1.5rem; font-weight: 800; color: var(--accent); }
        
        .log-container { font-family: monospace; font-size: 0.75rem; height: 220px; overflow-y: auto; background: #020617; padding: 10px; border-radius: 6px; }
        .log-entry { margin-bottom: 4px; color: #cbd5e1; border-bottom: 1px solid #1e293b; }
    </style>
</head>
<body>

<div class="wrapper">
    <div class="main-content">
        <h2>Wumpus Logic Environment</h2>
        <div class="controls">
            <input type="number" id="gSize" value="4" min="3" max="6">
            <button class="btn-new" onclick="resetGame()">New</button>
            <button class="btn-exec" onclick="runStep()">Execute Inference</button>
        </div>
        <div id="grid"></div>
    </div>

    <div class="sidebar">
        <div class="stat-card">
            <div class="stat-label">Inference Steps</div>
            <div id="stepsCount" class="stat-val">0</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Percepts</div>
            <div id="perceptDisplay" style="color: #fbbf24; font-weight: bold; font-size: 1rem;">None</div>
        </div>
        <div class="log-container" id="log"></div>
    </div>
</div>

<script>
    class InferenceEngine {
        constructor() { this.kb = []; this.count = 0; }
        tell(clause) { 
            const s = JSON.stringify(clause.sort());
            if (!this.kb.some(c => JSON.stringify(c.sort()) === s)) this.kb.push(clause);
        }
        ask(lit) {
            const query = lit.startsWith('-') ? [lit.substring(1)] : [`-${lit}`];
            let clauses = [...this.kb, query];
            let attempts = 0;
            while (attempts < 40) {
                let newClauses = [];
                for (let i = 0; i < clauses.length; i++) {
                    for (let j = i + 1; j < clauses.length; j++) {
                        this.count++;
                        const res = this.resolve(clauses[i], clauses[j]);
                        if (res === null) continue;
                        if (res.length === 0) return true;
                        newClauses.push(res);
                    }
                }
                const oldLen = clauses.length;
                clauses = [...new Set([...clauses, ...newClauses].map(c => JSON.stringify(c.sort())))].map(s => JSON.parse(s));
                if (clauses.length === oldLen) return false;
                attempts++;
            }
            return false;
        }
        resolve(c1, c2) {
            for (let l1 of c1) {
                for (let l2 of c2) {
                    if (l1 === `-${l2}` || l2 === `-${l1}`) {
                        return [...new Set([...c1.filter(x => x !== l1), ...c2.filter(x => x !== l2)])];
                    }
                }
            }
            return null;
        }
    }

    let size, grid, pos, engine, visited, active;

    function resetGame() {
        size = parseInt(document.getElementById('gSize').value);
        grid = Array(size).fill().map(() => Array(size).fill(null));
        visited = Array(size).fill().map(() => Array(size).fill(false));
        pos = { x: 0, y: 0 }; engine = new InferenceEngine(); active = true;
        for(let i=0; i<size; i++) for(let j=0; j<size; j++) {
            if(i===0 && j===0) continue;
            if(Math.random() < 0.18) grid[i][j] = 'P';
        }
        grid[size-1][size-1] = 'W';
        document.getElementById('log').innerHTML = "";
        render(); updateUI();
    }

    function runStep() {
        if (!active) return;
        visited[pos.x][pos.y] = true;
        let p = [];
        let neighbors = [[pos.x-1,pos.y],[pos.x+1,pos.y],[pos.x,pos.y-1],[pos.x,pos.y+1]]
                        .filter(([r,c]) => r>=0 && r<size && c>=0 && c<size);

        neighbors.forEach(([r,c]) => {
            if(grid[r][c] === 'P') p.push('Breeze');
            if(grid[r][c] === 'W') p.push('Stench');
        });

        if (!p.includes('Breeze')) neighbors.forEach(([r,c]) => engine.tell([`-P${r}${c}`]));
        if (!p.includes('Stench')) neighbors.forEach(([r,c]) => engine.tell([`-W${r}${c}`]));

        let moved = false;
        for (let [r,c] of neighbors) {
            if (!visited[r][c]) {
                if (engine.ask(`-P${r}${c}`) && engine.ask(`-W${r}${c}`)) {
                    pos = { x: r, y: c }; moved = true;
                    addLog(`Moved to [${r},${c}]`);
                    break;
                }
            }
        }
        if (grid[pos.x][pos.y]) { addLog("DEAD!"); active = false; }
        else if (!moved) { addLog("HALTED: No Safe Path"); active = false; }
        document.getElementById('perceptDisplay').innerText = p.join('+') || 'None';
        render(); updateUI();
    }

    function render() {
        const g = document.getElementById('grid');
        g.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
        g.innerHTML = '';
        for(let i=0; i<size; i++) for(let j=0; j<size; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            if (visited[i][j]) cell.classList.add('visited');
            if (engine.ask(`-P${i}${j}`) && engine.ask(`-W${i}${j}`)) cell.classList.add('safe-border');
            if (pos.x === i && pos.y === j) cell.innerHTML = '<div class="agent"></div>';
            if (!active && grid[i][j]) {
                cell.innerText = grid[i][j] === 'P' ? '🕳️' : '👹';
                cell.classList.add('hazard');
            }
            g.appendChild(cell);
        }
    }

    function addLog(msg) {
        const l = document.getElementById('log');
        l.innerHTML += `<div class="log-entry">> ${msg}</div>`;
        l.scrollTop = l.scrollHeight;
    }

    function updateUI() { document.getElementById('stepsCount').innerText = engine.count; }
    resetGame();
</script>
</body>
</html>
