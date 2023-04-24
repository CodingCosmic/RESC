import math
import os
import time

def display_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;31;40m  RRRR  \033[1;32;40m  EEEE  \033[1;33;40m  SSSS  \033[1;34;40m  CCCC  ")
    print("\033[1;31;40m  R   R \033[1;32;40m  E      \033[1;33;40m S       \033[1;34;40m C      ")
    print("\033[1;31;40m  RRRR  \033[1;32;40m  EEEE  \033[1;33;40m  SSSS  \033[1;34;40m  C      ")
    print("\033[1;31;40m  R  R  \033[1;32;40m  E      \033[1;33;40m      S \033[1;34;40m  C      ")
    print("\033[1;31;40m  R   R \033[1;32;40m  EEEE  \033[1;33;40m  SSSS  \033[1;34;40m  CCCC  \n\033[0m")
    print("\nThank you for using this tool to find your Helmholtz frequency!")
    print("If you would like to support, star, and like, show some love donate to paypal.me/cosmicspiritsupport")

def helmholtz_frequency(volume, opening_area, opening_length, end_correction=0.00, speed_of_sound=344):
    effective_opening_length = opening_length + end_correction
    resonant_frequency = (speed_of_sound / (2 * math.pi)) * math.sqrt((opening_area * effective_opening_length) / volume)
    return resonant_frequency

def main():
    display_header()
    first_run = True

    while True:
        if first_run:
            print("Helmholtz resonator: A resonator that amplifies sound by resonating at a specific frequency.\n")
            first_run = False
        else:
            display_header()

        print("Enter the volume (in cubic meters). Example values: 0.001 (small) to 10 (large)")
        volume = float(input("Volume: "))

        print("\nEnter the opening area (in square meters). Example values: 0.0001 (small) to 1 (large)")
        opening_area = float(input("Opening area: "))

        print("\nEnter the opening length (in meters). Example values: 0.01 (short) to 1 (long)")
        opening_length = float(input("Opening length: "))

        end_correction = input("\nEnter an optional end correction value (in meters) or press Enter to skip: ")
        if end_correction:
            end_correction = float(end_correction)
        else:
            end_correction = 0

        calculate = input("\nDo you want to calculate the Helmholtz resonator frequency? (y/n): ").lower()
        if calculate == 'y':
            frequency = helmholtz_frequency(volume, opening_area, opening_length, end_correction)
            print(f"\nThe Helmholtz resonator frequency is: {frequency} Hz\nBeautiful!")

        continue_choice = input("\nDo you want to continue? (y/n),")
if __name__ == "__main__":
    main()
