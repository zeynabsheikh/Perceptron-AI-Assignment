import tkinter as tk
from tkinter import messagebox
import random

class ResolutionEngine:
    def __init__(self):
        self.kb = [] 
        self.steps = 0

    def tell(self, clause):
        if sorted(clause) not in self.kb:
            self.kb.append(sorted(clause))

    def ask(self, literal):
        query = [literal[1:]] if literal.startswith('-') else ['-' + literal]
        clauses = list(self.kb) + [query]
        for _ in range(15): 
            new = set()
            for i in range(len(clauses)):
                for j in range(i + 1, len(clauses)):
                    self.steps += 1
                    res = self.resolve(clauses[i], clauses[j])
                    if res is not None:
                        if len(res) == 0: return True
                        if len(res) <= 2: new.add(tuple(sorted(res)))
            if not new or all(tuple(c) in [tuple(x) for x in clauses] for c in new): break
            for c in list(new): clauses.append(list(c))
        return False

    def resolve(self, c1, c2):
        for l1 in c1:
            for l2 in c2:
                if l1 == '-' + l2 or l2 == '-' + l1:
                    return list(set([x for x in c1 if x != l1] + [x for x in c2 if x != l2]))
        return None

class WumpusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wumpus World - Goal Search")
        self.size = 4
        self.agent_pos = [3, 0]
        self.gold_pos = [random.randint(0,2), random.randint(1,3)]
        self.hazards = {} # Stores Pits and Wumpus
        self.grid_status = {} # 1: Safe, 2: Danger, 3: Gold
        self.engine = ResolutionEngine()
        self.visited = {(3, 0)}
        self.setup_env()
        self.setup_ui()

    def setup_env(self):
        # Randomly place a few pits
        for _ in range(2):
            p = (random.randint(0,3), random.randint(0,3))
            if p != (3,0) and p != tuple(self.gold_pos): self.hazards[p] = "PIT"
        # Place Wumpus
        w = (random.randint(0,2), random.randint(0,3))
        if w != (3,0): self.hazards[w] = "WUMPUS"

    def setup_ui(self):
        self.header = tk.Frame(self.root, bg="#1a202c", pady=10)
        self.header.pack(fill="x")
        self.step_lbl = tk.Label(self.header, text="Inference Steps: 0", fg="#63b3ed", bg="#1a202c", font=("Arial", 11, "bold"))
        self.step_lbl.pack(side="left", padx=20)
        self.percept_lbl = tk.Label(self.header, text="Percept: None", fg="#ecc94b", bg="#1a202c", font=("Arial", 11, "bold"))
        self.percept_lbl.pack(side="right", padx=20)

        self.grid_fr = tk.Frame(self.root, pady=15)
        self.grid_fr.pack()
        self.btns = {}
        for r in range(self.size):
            for c in range(self.size):
                l = tk.Label(self.grid_fr, width=10, height=4, relief="ridge", bg="white", borderwidth=2)
                l.grid(row=r, column=c, padx=2, pady=2)
                self.btns[(r,c)] = l
        
        self.btn = tk.Button(self.root, text="Step Logic & Find Gold", command=self.move_agent, bg="#10b981", fg="white", font=("Arial", 12, "bold"))
        self.btn.pack(fill="x", padx=50, pady=10)
        self.update_view()

    def move_agent(self):
        r, c = self.agent_pos
        if [r, c] == self.gold_pos:
            messagebox.showinfo("Victory!", "Gold Found! Agent Wins.")
            return

        # Percept generation based on neighbors
        percept = "None"
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if (nr, nc) in self.hazards:
                percept = "Breeze" if self.hazards[(nr,nc)] == "PIT" else "Stench"
        self.percept_lbl.config(text=f"Percept: {percept}")

        self.engine.tell([f"-P{r}{c}"])
        self.grid_status[(r,c)] = 1
        
        adj = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        valid_moves = [m for m in adj if 0 <= m[0] < self.size and 0 <= m[1] < self.size]
        
        best_move = None
        for nr, nc in valid_moves:
            if self.engine.ask(f"-P{nr}{nc}"):
                self.grid_status[(nr,nc)] = 1
                if (nr, nc) not in self.visited:
                    best_move = (nr, nc)
                    break
            else:
                self.grid_status[(nr,nc)] = 2

        if best_move:
            self.agent_pos = list(best_move)
            self.visited.add(best_move)
        else:
            # Exploration
            unvisited = [m for m in valid_moves if m not in self.visited]
            if unvisited:
                self.agent_pos = list(random.choice(unvisited))
                self.visited.add(tuple(self.agent_pos))

        self.step_lbl.config(text=f"Inference Steps: {self.engine.steps}")
        self.update_view()

    def update_view(self):
        for (r, c), b in self.btns.items():
            color = "white"
            txt = ""
            if [r, c] == self.agent_pos: txt = "🤖\nAGENT"
            elif [r, c] == self.gold_pos and (r,c) in self.visited: 
                txt = "💰\nGOLD"
                color = "#fef3c7"
            elif self.grid_status.get((r,c)) == 1: color = "#c6f6d5"
            elif self.grid_status.get((r,c)) == 2: color = "#fed7d7"
            b.config(bg=color, text=txt)

if __name__ == "__main__":
    root = tk.Tk()
    app = WumpusApp(root)
    root.mainloop()
