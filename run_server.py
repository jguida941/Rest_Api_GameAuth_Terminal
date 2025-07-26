#!/usr/bin/env python3
import os
import subprocess
import time
import sys

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Clear the screen for better visibility
os.system('clear' if os.name == 'posix' else 'cls')

# Neon orange glowing ASCII art banner
print("\033[38;5;202m" + """
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░                                                                 ░
    ░  \033[38;5;208m██████╗  █████╗ ███╗   ███╗███████╗ █████╗ ██╗   ██╗████████╗██╗  ██╗\033[38;5;202m
    ░  \033[38;5;214m██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔══██╗██║   ██║╚══██╔══╝██║  ██║\033[38;5;202m
    ░  \033[38;5;208m██║  ███╗███████║██╔████╔██║█████╗  ███████║██║   ██║   ██║   ███████║\033[38;5;202m
    ░  \033[38;5;214m██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██║██║   ██║   ██║   ██╔══██║\033[38;5;202m
    ░  \033[38;5;208m╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝   ██║   ██║  ██║\033[38;5;202m
    ░  \033[38;5;214m ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝\033[38;5;202m
    ░                                                                 ░
░               \033[38;5;208m◆ ◇ ◆  REST API FOR GAME SERVER DEMO  ◆ ◇ ◆\033[38;5;202m              ░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""" + "\033[0m")

# Loading animation with cyber theme
print("\n\033[38;5;46m" + "⚡ Test the system by following the instructions below ⚡" + "\033[0m")
print("\033[38;5;239m" + "━" * 60 + "\033[0m")

loading_chars = ["◐", "◓", "◑", "◒"]
for i in range(20):
    progress = int((i + 1) * 3)
    bar = "\033[38;5;46m█\033[0m" * (progress // 5) + "\033[38;5;239m░\033[0m" * (12 - progress // 5)
    sys.stdout.write(f'\r\033[38;5;46m{loading_chars[i % len(loading_chars)]}\033[0m {bar} \033[38;5;46m{progress}%\033[0m LOADING...')
    sys.stdout.flush()
    time.sleep(0.08)

print("\r\033[38;5;46m✓\033[0m \033[38;5;46m████████████\033[0m \033[38;5;46m100%\033[0m Server Connected!                    ")

# Instructions with glowing red borders to match GAMEAUTH
print("\n\033[38;5;196m╔════════════════════════════════════════════════════════════╗\033[0m")
print("\033[38;5;196m║\033[0m                    \033[38;5;208mLogin Instructions\033[0m                     \033[38;5;196m║\033[0m")
print("\033[38;5;196m╠════════════════════════════════════════════════════════════╣\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[97mSimply:\033[0m                                                  \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Paste into browser: \033[93mlocalhost:8080\033[0m                     \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Use provided logins below to test the system           \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Test API endpoints and manage user data                \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m╠════════════════════════════════════════════════════════════╣\033[0m")
print("\033[38;5;196m║\033[0m                   \033[38;5;208mLogin Credentials\033[0m                       \033[38;5;196m║\033[0m")
print("\033[38;5;196m╠════════════════════════════════════════════════════════════╣\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[91mADMIN ACCESS:\033[0m                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Username: \033[91madmin\033[0m    \033[38;5;208m▸\033[0m Password: \033[91mpassword\033[0m                      \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[92mUSER ACCESS:\033[0m                                             \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Username: \033[92muser\033[0m     \033[38;5;208m▸\033[0m Password: \033[92mpassword\033[0m                      \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[94mPLAYER ACCESS:\033[0m                                           \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Username: \033[94mplayer\033[0m   \033[38;5;208m▸\033[0m Password: \033[94mpassword\033[0m                      \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[95mGUEST ACCESS:\033[0m                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Username: \033[95mguest\033[0m    \033[38;5;208m▸\033[0m Password: \033[95mpassword\033[0m                      \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m                                                            \033[38;5;196m║\033[0m")
print("\033[38;5;196m╠════════════════════════════════════════════════════════════╣\033[0m")
print("\033[38;5;196m║\033[0m                    \033[38;5;208mAPI Endpoints\033[0m                          \033[38;5;196m║\033[0m")
print("\033[38;5;196m╠════════════════════════════════════════════════════════════╣\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Main Login Page: \033[93mhttp://localhost:8080/gameusers\033[0m               \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Status Check: \033[93mhttp://localhost:8080/status\033[0m                     \033[38;5;196m║\033[0m")
print("\033[38;5;196m║\033[0m  \033[38;5;208m▸\033[0m Health Monitor: \033[93mhttp://localhost:8081/healthcheck\033[0m              \033[38;5;196m║\033[0m")
print("\033[38;5;196m╠════════════════════════════════════════════════════════════╣\033[0m")
print("\033[38;5;196m║\033[0m         Press \033[91mCtrl+C\033[0m to terminate server connection        \033[38;5;196m║\033[0m")
print("\033[38;5;196m╚════════════════════════════════════════════════════════════╝\033[0m")

print("\n\033[38;5;208m╔════════════════════════════════════════════════════════════╗\033[0m")
print("\033[38;5;208m║           LAUNCHING AUTHENTICATION SERVER                  ║\033[0m")
print("\033[38;5;208m╚════════════════════════════════════════════════════════════╝\033[0m")

# Pulsing effect simulation
for i in range(3):
    sys.stdout.write(f'\r\033[38;5;{202 + (i % 3) * 2}m● ● ● CONNECTING TO AUTHENTICATION MATRIX ● ● ●\033[0m')
    sys.stdout.flush()
    time.sleep(0.3)

print("\r\033[38;5;46m✓ CONNECTION ESTABLISHED: http://localhost:8080/gameusers                               \033[0m")
print("\n\033[38;5;239m" + "─" * 60)
print("\033[38;5;245mServer logs will appear below (this is normal!):\033[0m")
print("\033[38;5;239m" + "─" * 60 + "\033[0m\n")

# Run the Java server (this will run until you stop it)
subprocess.run(["java", "-jar", "target/gameauth-0.0.1-SNAPSHOT.jar", "server", "config.yml"])