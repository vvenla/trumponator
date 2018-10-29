"""
@InProceedings{joulin2017bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  booktitle={Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers},
  month={April},
  year={2017},
  publisher={Association for Computational Linguistics},
  pages={427--431},
}
"""

import fasttext
import sys

MODEL_DIR = "models/"

model = fasttext.load_model(MODEL_DIR + 'all_model.bin')

#print (model.labels)

if len(sys.argv) > 1:
    tweet = sys.argv[1]
    print("Predict the stock reacton for tweet:\n\t", tweet)
    print()
    pred = model.predict(tweet)
    pred = pred[0][0] #take the label out of lists
    pred = pred[9:] #remove the "__label__" from front of it
    print ("The stock will change " + pred + " on the next business day!")
else:
    print ("You didn't give a tweet to predict from!")

