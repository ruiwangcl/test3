from absl import flags
from absl import logging
from absl import app
FLAGS = flags.FLAGS

flags.DEFINE_string("model", None, "model to run") # name ,default, help

def main(argv):
   print("hello, world")
   # logging.info(‘selected model’,FLAGS.model)
   print("selected model", FLAGS.model)

if __name__ == "__main__":
   app.run(main)