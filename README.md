# 🕵️‍♂️ Dynamic Wumpus Logic Agent (Resolution Engine)

## 📌 Overview
This project is a **Knowledge-Based Agent** designed to navigate the classic "Wumpus World" environment. The core strength of this agent lies in its ability to not just find a path, but to "deduce" the safety of its next move using **Propositional Logic** and a **Resolution Refutation** engine.

The application is built using Python and **Tkinter**, featuring a modern dashboard to visualize the agent's reasoning process, inference steps, and environmental percepts in real-time.

---

## 🎯 Key Objectives
* **Logical Reasoning:** The agent utilizes environmental percepts (Breezes & Stenches) to navigate the grid safely.
* **Propositional Logic KB:** A dynamic Knowledge Base that updates rules via **TELL** and **ASK** functions during each move.
* **Automated Inference:** Implementation of the Resolution Refutation algorithm to mathematically prove cell safety.
* **Real-Time Visualization:** A professional dashboard tracking inference steps, current percepts, and agent movement.

---

## ⚙️ Technologies Used
* **Python 3.x:** Core programming language.
* **Tkinter:** Used for Desktop GUI development.
* **Propositional Logic:** For formal representation of environmental constraints and rules.

---

## 🧠 Algorithmic Implementation

### 1. The Knowledge Base (KB)
At every cell, the agent **TELLS** the KB about its observations:
* **Breeze:** If a Breeze is detected, the KB deduces that a Pit may exist in adjacent cells.
* **Stench:** If a Stench is detected, it implies the Wumpus might be in an adjacent cell.
* **Safety:** When an agent occupies a cell, it confirms that specific coordinate is safe.

### 2. Resolution Refutation
Before moving, the agent **ASKS** the KB if a target cell is safe (Prove: $\neg Pit \land \neg Wumpus$):
1.  The query is negated.
2.  The KB and the negated query are converted into clauses (CNF).
3.  The engine resolves pairs of clauses to find a **contradiction (empty clause)**. If found, the cell is logically proven safe.

---

## 📊 Environment Specifications
* **Agent (🤖):** A logic-based bot navigating the grid.
* **Safe Cells (Green):** Cells that have been 100% logically proven safe.
* **Hazard Cells (Red):** Cells where the logic indicates a potential Pit or Wumpus.
* **Gold (💰):** The agent's primary objective, hidden within the grid.

---

## 🧪 How to Run
1.  **Save the Script:**
    Save the provided code as `python.py` in your project folder.
2.  **Run the Application:**
    Open your terminal or CMD and run:
    ```bash
    python wumpus.py
    ```
3.  **Interact:** 
    * Click the **"Step Logic & Find Gold"** button.
    * Watch the agent analyze neighbors and mark safe cells in **Green**.
    * A victory message will appear once the agent successfully reaches the **Gold**.

---

## 📝 Author
**Zainab Noor**  
National University of Computer & Emerging Sciences (FAST-NUCES)
