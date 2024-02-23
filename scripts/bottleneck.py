import cProfile
import subprocess

def main():
    bash_script = "./automation.sh"
    cProfile.run('subprocess.call(["' + bash_script + '"], shell=True)')


if __name__ == "__main__":
    main()

