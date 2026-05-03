# 🕵️‍♂️ Dynamic Wumpus Logic Agent (Web App)

## 📌 Overview
This project is a web-based **Knowledge-Based Agent** designed to navigate the classic "Wumpus World" environment. Unlike simple pathfinders, this agent utilizes **Propositional Logic** and an automated **Resolution Refutation** engine to deduce safe moves in a grid filled with hidden hazards.

The application is built as a single-file web solution, integrating a complex logic parser, a reasoning engine, and a dynamic UI to visualize the agent's decision-making process in real-time.

---

## 🎯 Key Objectives
*   **Dynamic Environment:** Support for user-defined grid dimensions and randomized hazard (Pits & Wumpus) placement.
*   **Propositional Logic KB:** Maintaining a Knowledge Base that stores rules based on environmental percepts (Breezes & Stenches).
*   **Inference Engine:** Implementing a Resolution Refutation algorithm to prove cell safety by converting logic to Conjunctive Normal Form (CNF).
*   **Real-Time Visualization:** A professional dashboard tracking inference steps, active percepts, and agent logs.

---

## ⚙️ Technologies Used
*   **HTML5 & CSS3:** For a professional, responsive dashboard and grid visualization.
*   **Vanilla JavaScript (ES6+):** Core logic for the Resolution Engine and Environment simulation.
*   **Propositional Logic:** Used for formal representation of environmental constraints.

---

## 🧠 Algorithmic Implementation

### 1. The Knowledge Base (KB)
The agent operates by **TELLING** the KB about its observations:
*   **Breeze:** Implies a Pit is in an adjacent cell.
*   **Stench:** Implies the Wumpus is in an adjacent cell.
*   **Safety:** If no percept is found, the agent deduces that all adjacent cells are safe from that specific hazard.

### 2. Resolution Refutation
Before every move, the agent **ASKS** the KB if a target cell is safe (Prove $\neg Pit \land \neg Wumpus$). The engine:
1.  Negates the query.
2.  Converts the KB and negated query into **CNF**.
3.  Resolves clauses to find a **contradiction (empty clause)**, confirming the cell's safety.

---

## 📊 Environment Specifications
*   **Agent:** Represented by the gold icon.
*   **Safe Cells:** Highlighted with a green border once logically proven.
*   **Hazards:** Pits (●) and the Wumpus (▲) are revealed only if the agent enters their cell or the game halts.

---

## 🧪 How to Run
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/zeynabsheikh/Wumpus-Logic-Agent.git](https://github.com/zeynabsheikh/Wumpus-Logic-Agent.git)
    ```
2.  **Open the App:** Simply double-click `index.html` to run the application in any modern web browser.
3.  **Interact:** Set the grid size, click **New Environment**, and use **Execute Inference Step** to watch the agent reason through the grid.

---


### **LinkedIn Post Reference**
Watch the agent's reasoning process in action on my LinkedIn:  
**[PASTE YOUR LINKEDIN POST URL HERE]**
