# 🕵️‍♂️ Dynamic Wumpus Logic Agent (Resolution Engine)

## 📌 Overview
Ye project aik **Knowledge-Based Agent** hai jo classic "Wumpus World" environment mein navigate karta hai. Is project ki khususiyt ye hai ke ye sirf rasta nahi dhundta, balkay **Propositional Logic** aur **Resolution Refutation** engine ko use karte hue ye "deduce" karta hai ke agla qadam safe hai ya nahi.

Application ko Python aur **Tkinter** mein banaya gaya hai taake aik modern dashboard ke zariye agent ki reasoning, inference steps, aur environmental percepts ko real-time visualize kiya ja sakay.

---

## 🎯 Key Objectives
* **Logical Reasoning:** Agent environmental percepts (Breezes & Stenches) ko use kar ke rasta nikalta hai.
* **Propositional Logic KB:** Aik dynamic Knowledge Base jo har move par rules ko **TELL** aur **ASK** functions ke zariye update karti hai.
* **Automated Inference:** Resolution Refutation algorithm ka istemal kar ke cell safety ko mathematically prove karna.
* **Real-Time Visualization:** Dashboard jo inference steps, current percepts aur agent ki movement ko track karta hai.

---

## ⚙️ Technologies Used
* **Python 3.x:** Core programming language.
* **Tkinter:** Desktop GUI development ke liye.
* **Propositional Logic:** Environmental constraints aur rules ki formal representation ke liye.

---

## 🧠 Algorithmic Implementation

### 1. The Knowledge Base (KB)
Agent har cell par ja kar KB ko **TELL** karta hai:
* **Breeze:** Agar Breeze mile, to KB deduce karti hai ke adjacent cells mein Pit ho sakta hai.
* **Stench:** Agar Stench mile, to adjacent cells mein Wumpus ka khatra hota hai.
* **Safety:** Jab agent kisi cell par hota hai, to wo confirm karta hai ke wo cell safe hai.

### 2. Resolution Refutation
Move karne se pehle agent KB se **ASK** karta hai (Prove: $\neg Pit \land \neg Wumpus$):
1.  Query ko negate kiya jata hai.
2.  KB aur negated query ko clauses mein convert kiya jata hai.
3.  Engine pairs of clauses ko **resolve** kar ke contradiction dhundta hai. Agar empty clause mil jaye, to cell safe prove ho jata hai.

---

## 📊 Environment Specifications
* **Agent (🤖):** Grid mein navigate karne wala logic-based bot.
* **Safe Cells (Green):** Wo cells jo logic ke zariye 100% safe prove ho chuke hain.
* **Hazard Cells (Red):** Wo cells jahan logic ke mutabiq Pit ya Wumpus hone ka imkan hai.
* **Gold (💰):** Agent ka main target jo grid mein kahin bhi hidden ho sakta hai.

---

## 🧪 How to Run
1.  **Repository Clone Karein ya File Save Karein:**
    Apne computer par `python.py` file save karein.
2.  **Script Run Karein:**
    Terminal ya CMD mein niche di gayi command likhen:
    ```bash
    python python.py
    ```
3.  **Interact:** * **Execute Logic & Find Gold** button par click karein.
    * Agent automatically neighbors ko analyze karega aur safe cells ko **Green** mark karega.
    * Jab agent Gold wale cell par pohanchega, to Victory message show hoga.

---

## 📝 Author
**Zainab Noor** National University of Computer & Emerging Sciences (FAST-NUCES)
