#  PortKnockReveal – A Beginner's Journey into Stealthy Ports

> "Do as I do, YO! My second ethical hacking project."

This is a beginner-friendly project exploring **port knocking**, a technique used to hide services until a specific port sequence is accessed.



#  What is Port Knocking?

Port knocking is like a secret handshake. You "knock" on a sequence of ports, and if you get it right, a hidden port (like SSH) opens.

---



#  Features

-  Simulates knocking on ports with Bash and Python
-  Detects knocking attempts (fake/mockup style)
-  Scans with Nmap to find hidden services
-  100% beginner-friendly!

---



# Project Structure

```
PortKnockReveal/
├── README.md
├── port_knocking_detector.py
├── knocking_simulation.sh
├── test_vm_setup.md
├── scans/
│   └── knock_detect.txt
├── .gitignore
```

---

#  Run the Simulation

# ▶ Python Knock

```bash
python3 port_knocking_detector.py
```

# ▶ Bash Knock

```bash
bash knocking_simulation.sh
```

---

# 🔍 Scan with Nmap

```bash
nmap -p- 127.0.0.1 -oN scans/knock_detect.txt
```

---

# For Learning Only

This project is **educational**. Test only on systems you control. Inspired by TryHackMe.

#   P o r t K n o c k R e v e a l 
 
 
