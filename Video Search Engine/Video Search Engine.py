import speech_recognition as sr
import moviepy.editor as mp
import re

def find_dialog_occurrences(video_path, target_dialog, output_path):
    recognizer = sr.Recognizer()

  
    video_clip = mp.VideoFileClip(video_path) # Loading the video file
    audio_clip = video_clip.audio

    
    recognized_text = recognizer.recognize_sphinx(audio_clip)

  
    occurrences = [m.start() for m in re.finditer(re.escape(target_dialog), recognized_text, flags=re.IGNORECASE)]

   
    print(f"Occurrences of '{target_dialog}' in the video:")
    for start_position in occurrences:
        print(f"- Found at {start_position} seconds")

   
    with open("occurrence_positions.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(map(str, occurrences)))

    
    with open("recognized_text.txt", "w", encoding="utf-8") as file:
        file.write(recognized_text)

if __name__ == "__main__":
    video_input_path = input("Enter the video file path: ")
    target_dialog = input("Enter the word you want to search: ")
    output_audio_path = input("Enter a desired output file path for the audio file: ")

    find_dialog_occurrences(video_input_path, target_dialog, output_audio_path)