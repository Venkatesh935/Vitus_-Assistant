import os
import sys

def manage_startup(enable=True):
    # Locate the hidden Windows Startup Folder securely
    startup_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    vbs_path = os.path.join(startup_dir, "Vitus_Startup.vbs")
    
    if enable:
        # Dynamically grab the absolute path to your project
        project_dir = os.path.dirname(os.path.abspath(__file__))
        run_script = os.path.join(project_dir, "run.bat")
        
        # Write a VBScript to launch run.bat silently (0 = hide window)
        content = f'Set WshShell = CreateObject("WScript.Shell")\n'
        content += f'WshShell.Run chr(34) & "{run_script}" & Chr(34), 0\n'
        content += f'Set WshShell = Nothing\n'
        
        try:
            with open(vbs_path, "w") as f:
                f.write(content)
            print("\n✅ SUCCESS: Vitus has been added to Windows Startup!")
            print("The graphical interface will now launch automatically when you log into Windows.")
        except Exception as e:
            print(f"\n❌ Failed to add to startup: {e}")
            
    else:
        if os.path.exists(vbs_path):
            try:
                os.remove(vbs_path)
                print("\n✅ SUCCESS: Vitus has been removed from Windows Startup.")
            except Exception as e:
                print(f"\n❌ Failed to remove from startup: {e}")
        else:
            print("\nVitus is not currently in the Windows Startup folder.")

if __name__ == "__main__":
    print("=======================================")
    print("      VITUS STARTUP CONFIGURATION")
    print("=======================================")
    print("1. Enable Vitus on Windows Startup")
    print("2. Disable Vitus on Windows Startup")
    print("3. Exit")
    print("=======================================")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        manage_startup(enable=True)
    elif choice == "2":
        manage_startup(enable=False)
    else:
        print("Exiting...")