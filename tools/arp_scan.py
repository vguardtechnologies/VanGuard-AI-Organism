from langchain.tools import tool
import subprocess
import platform

@tool("arp_scan_terminal", return_direct=True)
def arp_scan_terminal() -> str:
    """
    Runs 'arp -a' in a new Terminal window on macOS.
    Example queries:
    - "Show me the ARP table"
    - "Run arp scan"
    - "Find all devices on my network"
    """
    system = platform.system()

    if system == "Darwin":
        apple_script = '''
        tell application "Terminal"
            activate
            do script "arp -a"
        end tell
        '''
        try:
            subprocess.Popen(["osascript", "-e", apple_script])
            return "Absolutely sir! All devices on your network are now being listed in your Terminal. What else can I help with?"
        except Exception as e:
            return f"Failed to open Terminal: {str(e)}"

    else:
        return f"⚠️ ARP scan in terminal only implemented for macOS Terminal, not {system}."
