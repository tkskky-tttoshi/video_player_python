import cv2
import time
import datetime
import numpy as np

class Display:
    def __init__(self):
        self.input_key_array = ['a', 'b', 'c']
        pass

    def return_file_name(self, input_value):
        file_name = ''
        if input_value == self.input_key_array[0]:
            file_name = 'video/parkmovie.mp4'
        elif input_value == self.input_key_array[1]:
            file_name = 'video/roadmovie.mp4'
        elif input_value == self.input_key_array[2]:
            file_name = 'video/black.mp4'
        return file_name

    def print_typing_time(self):
        dt_now = datetime.datetime.now()
        print(dt_now)

    def display_image(self):
        pass

    def play_video(self, file_name):
        video_file = cv2.VideoCapture(file_name)
        file_name = ''
        fps = 30
        flag = False
        while(video_file.isOpened()):
            ret, frame = video_file.read()
            frame = cv2.resize(frame, dsize=(640, 640))
            if ret:
                cv2.imshow(file_name, frame)
            else:
                print('No Frames')
                break
            key = cv2.waitKey(fps) & 0xFF
            if key == ord('q'):
                break
            if key == ord(self.input_key_array[0]):
                file_name = self.return_file_name(self.input_key_array[0])
                print('Now parkmovie.mp4 on Air')
                self.print_typing_time()
                flag = True
                break
            if key == ord(self.input_key_array[1]):
                file_name = self.return_file_name(self.input_key_array[1])
                print('Now roadmovie.mp4 on Air')
                self.print_typing_time()
                flag = True
                break

            if key == ord(self.input_key_array[2]):
                file_name = self.return_file_name(self.input_key_array[2])
                print('Now black.mp4 on Air')
                self.print_typing_time()
                flag = True
                break

        if flag == True:
            self.play_video(file_name)

        video_file.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    i = 0
    display = Display()
    while 1:
        i = i + 1
        print(i)
        input_key = input()
        flag = None
        if input_key == display.input_key_array[0]:
            file_name = display.return_file_name(input_key)
            flag = True
        elif input_key == display.input_key_array[1]:
            file_name = display.return_file_name(input_key)
            flag = True
        elif input_key == display.input_key_array[2]:
            file_name = display.return_file_name(input_key)
            flag = True

        if flag == True:
            display.play_video(file_name)



