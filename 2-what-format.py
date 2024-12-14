import sys

version = sys.version_info
python_version = version.major + version.minor/100
print("The Python version is {}.{}.{}".format(version.major, version.minor, version.micro))
print(f"The Python version is {python_version}")
print(f"The Python version is {version.major}.{version.minor}.{version.micro}")