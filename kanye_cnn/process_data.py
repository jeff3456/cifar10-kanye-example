import os
import tensorflow as tf
# Preprocess files in both kanye pics and non kanye pics;

pathtodata = (os.path.dirname(os.path.realpath(__file__))+
              '/../kanye_west_data/')

WIDTH = 450
HEIGHT = 300

NUM_CLASSES = 1

NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = 3000
NUM_EXAMPLES_PER_EPOCH_FOR_EVAL = 1000

TEST_FILE_NAME = pathtodata+'resized_kanye_pics/Kanye1.jpg'

tf.app.flags.DEFINE_string('directory', pathtodata,
                           'Directory to download data files and write the result')

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))



def get_kanye_f_names():
    i = 1
    basejpg = pathtodata+'resized_kanye_pics/Kanye{}.jpg'
    basejpeg = pathtodata+'resized_kanye_pics/Kanye{}.jpeg'
    fnames = []
    while(os.path.isfile(basejpg.format(i)) or os.path.isfile(basejpeg.format(i))):
        if(os.path.isfile(basejpg.format(i))):
            fnames.append(basejpg.format(i))
        else:
            fnames.append(basejpeg.format(i))

        i += 1
    return fnames

def get_not_kanye_f_names():
    i = 1
    basepng = pathtodata+'resized_not_kanye_pics/File{}.png'
    basejpg = pathtodata+'resized_not_kanye_pics/File{}.jpg'
    fnames = []
    while(os.path.isfile(basepng.format(i)) or
          os.path.isfile(basejpg.format(i))):
        if(os.path.isfile(basepng.format(i))):
            fnames.append(basepng.format(i))
        else:
            fnames.append(basejpg.format(i))
        i += 1
    return fnames






"""Another approach is to convert whatever data you have into a supported format.
This approach makes it easier to mix and match data sets and network architectures.
The recommended format for TensorFlow is a TFRecords file containing tf.train.Example
protocol buffers (which contain Features as a field). You write a little
program that gets your data, stuffs it in an Example protocol buffer,
serializes the protocol buffer to a string,
and then writes the string to a TFRecords file
using the tf.python_io.TFRecordWriter class.
For example,
tensorflow/examples/how_tos/reading_data/convert_to_records.py
converts MNIST data to this format."""

def read_kanye_pics(filename_queue, label):
    """reads and parses examples from kanye images."""

    class KanyeRecord():
        pass



