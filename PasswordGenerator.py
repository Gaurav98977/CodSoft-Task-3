#CodSoft Task 3
import random

def generate_password(length):
  # It Generates a random password of the specified length."""
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

def main():
  #Gives user for the desired password length and prints the generated password."""
  length = int(input("Enter the desired password length: "))
  password = generate_password(length)
  print("Your password is:", password)

if __name__ == "__main__":
  main()