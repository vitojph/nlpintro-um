import random
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator
from featureextractor import FeatureExtractor
from transition import Transition

if __name__ == '__main__':
    print('Loading training sets... ')
    # EN_data = dataset.get_english_train_corpus().parsed_sents()
    # random.seed('english')
    # EN_subdata = random.sample(EN_data, 200)
    # print('EN')

    # SE_data = dataset.get_swedish_train_corpus().parsed_sents()
    # random.seed('swedish')
    # SE_subdata = random.sample(SE_data, 200)
    # print('SE')
    #
    DK_data = dataset.get_danish_train_corpus().parsed_sents()
    random.seed('danish')
    DK_subdata = random.sample(DK_data, 200)
    print('DK')

    try:
        # EN
        # print('Saving EN model... ')
        # tp = TransitionParser(Transition, FeatureExtractor)
        # tp.train(EN_subdata)
        # tp.save('english.model')
        # print('Ok')
        # print('Parsing dev corpus...')
        # EN_testdata = dataset.get_english_dev_corpus().parsed_sents()
        # EN_tp = TransitionParser.load('english.model')
        # EN_parsed = EN_tp.parse(EN_testdata)
        # print('Ok')

        # # SE
        # tp = TransitionParser(Transition, FeatureExtractor)
        # tp.train(SE_subdata)
        # tp.save('swedish.model')
        # SE_testdata = dataset.get_swedish_test_corpus().parsed_sents()
        # SE_tp = TransitionParser.load('swedish.model')
        # SE_parsed = SE_tp.parse(SE_testdata)
        #
        # DK
        tp = TransitionParser(Transition, FeatureExtractor)
        print('Training...')
        tp.train(DK_subdata)
        print('Ok. Saving the model...')
        tp.save('danish.model')
        print('Ok. Parsing the test corpus...')
        DK_testdata = dataset.get_danish_test_corpus().parsed_sents()
        #DK_tp = TransitionParser.load('danish.model')
        DK_parsed = tp.parse(DK_testdata)
        print('Ok.')


        # with open('english.conll', 'w') as f:
        #     for p in EN_parsed:
        #         f.write(p.to_conll(10).encode('utf-8'))
        #         f.write('\n')
        #
        # ev = DependencyEvaluator(EN_testdata, EN_parsed)
        # print('Evaluating EN model...')
        # print "LAS: {} \nUAS: {}".format(*ev.eval())

        with open('danish.conll', 'w') as f:
            for p in DK_parsed:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev = DependencyEvaluator(DK_testdata, DK_parsed)
        print('Evaluating DK model...')
        print "LAS: {} \nUAS: {}".format(*ev.eval())

        # parsing arbitrary sentences (english):
        # sentence = DependencyGraph.from_sentence('Hi, this is a test')

        # tp = TransitionParser.load('english.model')
        # parsed = tp.parse([sentence])
        # print parsed[0].to_conll(10).encode('utf-8')
    except NotImplementedError:
        print """
        This file is currently broken! We removed the implementation of Transition
        (in transition.py), which tells the transitionparser how to go from one
        Configuration to another Configuration. This is an essential part of the
        arc-eager dependency parsing algorithm, so you should probably fix that :)

        The algorithm is described in great detail here:
            http://aclweb.org/anthology//C/C12/C12-1059.pdf

        We also haven't actually implemented most of the features for for the
        support vector machine (in featureextractor.py), so as you might expect the
        evaluator is going to give you somewhat bad results...

        Your output should look something like this:

            LAS: 0.23023302131
            UAS: 0.125273849831

        Not this:

            Traceback (most recent call last):
                File "test.py", line 41, in <module>
                    ...
                    NotImplementedError: Please implement shift!


        """
