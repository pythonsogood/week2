def prerequisites():
    try:
        import sys
        if sys.version_info < (3, 8):
            raise RuntimeError("Python 3.8 or higher is required.")

        import os
        import requests
        print("All prerequisites are satisfied.")
        return True
    except ImportError as e:
        print(f"Missing module: {e}. Please install required dependencies.")
        return False
    except RuntimeError as e:
        print(f"Prerequisite check failed: {e}")
        return False

if __name__ == "__main__":
    prerequisites()