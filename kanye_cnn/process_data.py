import os
import tensorflow as tf
from PIL import Image
import numpy as np
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

def convert_to(filename_queue):
    tf_filename_queue = tf.train.string_input_producer(filename_queue[:1]) #  list of files to read

    reader = tf.WholeFileReader()
    key, value = reader.read(tf_filename_queue)

    my_img = tf.image.decode_jpeg(value) # use png or jpg decoder based on your files.

    init_op = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init_op)

    # Start populating the filename queue.
    with sess.as_default():
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)

        for i in range(1): #length of your filename list
            image = my_img.eval() #here is your image Tensor :)

    print(image.shape)
    Image.fromarray(np.asarray(image)).show()
    coord.request_stop()
    coord.join(threads)


    # images = data_set.images
    # labels = data_set.labels
    # num_examples = data_set.num_examples

    # if images.shape[0] != num_examples:
    #     raise ValueError('Images size %d does not match label size %d.' %
    #                     (images.shape[0], num_examples))

    # rows = images.shape[1]
    # cols = images.shape[2]
    # depth = images.shape[3]
    # filename = os.path.join(FLAGS.directory, name + '.tfrecords')
    # print('Writing', filename)
    # writer = tf.python_io.TFRecordWriter(filename)
    # for index in range(num_examples):
    #     image_raw = images[index].tostring()
    #     example = tf.train.Example(features=tf.train.Features(feature={
    #         'height': _int64_feature(rows),
    #         'width': _int64_feature(cols),
    #         'depth': _int64_feature(depth),
    #         'label': _int64_feature(int(labels[index])),
    #         'image_raw': _bytes_feature(image_raw)}))
    #     writer.write(example.SerializeToString())
    # writer.close()


if __name__=="__main__":
    # get file names

    filename_queue = get_kanye_f_names()
    print('Length of filename queue: ', len(filename_queue))

    convert_to(filename_queue)
