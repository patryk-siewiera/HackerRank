# 5 kyu
import unittest


# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

class MyFirstTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')

    def test_2(self):
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')

    def test_3(self):
        self.assertEqual(pig_it('Quis custodiet ipsos custodes ?'), 'uisQay ustodietcay psosiay ustodescay ?')


def pig_it(text):
    text = text.split()
    output = []

    for word in text:
        output.append(word[1:] + word[0] + "ay")

    output = " ".join(output)
    if not output[-4].isalpha():
        output = output[:-2]
    return output


# print(pig_it('This is my strin!'))
unittest.main()
