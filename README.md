# Seven-bot-seven
A botnet utilizing polymorphic decryption along with c&amp;c server that can deploy keylogger take screenshots escalate privileges and remotely execute commands

For a step by step guide on how to deploy the botnet follow this link: https://dev.to/triple7/how-to-use-the-botnet-simulation-project-a-step-by-step-guide-pbf

I wanted to do this because B.Y.O.B. I liked alot but it never really worked and so I wanted to create something that would actually be something people could use

This project simulates a botnet in an educational setting, showing how a system can be compromised and controlled remotely. The setup begins with a malicious PDF file, which contains JavaScript that, when opened, triggers the download of a bot payload from a remote server. The downloaded bot is encrypted using a technique called polymorphic encryption, which makes slight modifications to the decryption process each time it runs, helping it evade detection by antivirus software.

Once the bot is downloaded and decrypted, it connects back to a Command and Control (C&C) server, which allows an attacker to issue commands remotely. The bot has several capabilities:

	1.	Keylogging: It can capture and log keystrokes from the infected machine.
	2.	Network Scanning: It can scan the local network to gather information about other devices connected to it.
	3.	Privilege Escalation: It downloads and runs tools like winPEAS and WES-NG to identify potential vulnerabilities in the system that could allow it to gain higher privileges, like administrator access. The results from these tools are sent back to the C&C server.
	4.	Screenshot Capture: It can take screenshots of the infected machine’s desktop.
	5.	Payload Execution: The bot can also execute arbitrary commands sent by the C&C server.

The C&C server is a Python script that listens for connections from the bot, allowing the attacker to issue commands and receive responses. For example, after running the privilege escalation tools, the attacker can analyze the results and decide on the next steps, such as deploying additional malware or exploiting specific vulnerabilities identified.

Overall, this simulation provides a detailed look at how an attacker might compromise a system, escalate their privileges, and maintain control, all while avoiding detection using advanced techniques. This setup is strictly for educational purposes and helps cybersecurity professionals understand and defend against these types of attacks.
