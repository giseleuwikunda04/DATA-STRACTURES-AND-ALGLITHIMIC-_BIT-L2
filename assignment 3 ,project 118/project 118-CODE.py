from collections import deque

print("=== STACK QUESTIONS ===")

# UR pushes ["Lecture1", "Lecture2", "Lecture3"]. Undo one. Which is top?
stack_ur = []
stack_ur.append("Lecture1")
stack_ur.append("Lecture2")
stack_ur.append("Lecture3")
stack_ur.pop()
print("UR Top of stack:", stack_ur[-1])  # Output: Lecture2

# In Irembo, push ["FormX", "FormY", "FormZ"]. Undo all. Which remains?
stack_irembo = []
stack_irembo.append("FormX")
stack_irembo.append("FormY")
stack_irembo.append("FormZ")
stack_irembo.pop()
stack_irembo.pop()
stack_irembo.pop()
print("Irembo Stack contents:", stack_irembo)  # Output: []

# Challenge: Push ["A", "B", "C"], pop 2, push "D". Which is top?
stack_challenge = []
stack_challenge.append("A")
stack_challenge.append("B")
stack_challenge.append("C")
stack_challenge.pop()
stack_challenge.pop()
stack_challenge.append("D")
print("Challenge Top of stack:", stack_challenge[-1])  # Output: D

print("\n=== QUEUE QUESTIONS ===")

# Airtel: 7 clients queue. After 2 served, who is front?
queue_airtel = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7"])
queue_airtel.popleft()
queue_airtel.popleft()
print("Airtel Front of queue:", queue_airtel[0])  # Output: Client3

# Nyabugogo: 10 buses queue. Who is last served?
queue_nyabugogo = deque([f"Bus{i}" for i in range(1, 11)])  # Bus1 to Bus10
print("Nyabugogo Last served:", queue_nyabugogo[-1])  # Output: Bus10
