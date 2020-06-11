import os
import shutil
import face_detection
import sampler
import trainer
import face_identification

def create_directories_to_run():
    path1 = os.getcwd() + '\\trainer'
    path2 = os.getcwd() + '\\dataset'

    try:
        os.mkdir(path1)
        os.mkdir(path2)
    except OSError:
        print('directory creation failed')
    else:
        print('directory creation worked')


def delete_directories():
    path1 = os.getcwd() + '\\trainer'
    path2 = os.getcwd() + '\\dataset'

    shutil.rmtree(path1)
    shutil.rmtree(path2)
    os.remove('names.txt')


def capabilities():
    print('Welcome to the face Identification system, it has been created through the utilization of solely openCV '
          'library')
    print('\n the options available are:')
    print('\n a. Open a simple face detector')
    print('\n b. Train your model to recognize your face')
    print('\n c. Access your specialized model')


def check_files_exist():
    path1 = os.getcwd() + '\\trainer'
    path2 = os.getcwd() + '\\dataset'
    suc = False

    if os.path.exists(path1) and os.path.exists(path2) and os.path.isfile('names.txt'):
        suc = True

    if suc and os.listdir(path1) == [] and os.listdir(path2) == []:
        suc = False

    return suc


def load_names():
    with open('names.txt', 'r') as f:
        names = [line.strip() for line in f]

    return names


while True:
    capabilities()
    order = input('Please select what you want to do, just input the letter you want: ')

    if order == 'a':
        face_detection.face_detection()

    elif order == 'b' and not check_files_exist():
        create_directories_to_run()
        sampler.sample()
        trainer.run_training()
        print('\n Training has been completed')

    elif order == 'b' and check_files_exist():
        answer = input('Do you want to override the existing trained model? y/n ')

        if answer == 'y':
            delete_directories()
            create_directories_to_run()
            sampler.sample()
            trainer.run_training()
            print('\n Training has been completed')

    elif order == 'c' and check_files_exist():
        face_identification.face_identification(load_names())
    elif order == 'q':
        quit()
    else:
        print('Your input is false, please resubmit your input')
