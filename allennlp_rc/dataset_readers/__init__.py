"""
Reading comprehension is loosely defined as follows: given a question and a passage of text that
contains the answer, answer the question.

These submodules contain readers for things that are predominantly reading comprehension datasets.
"""

from allennlp_rc.dataset_readers.drop import DropReader
from allennlp_rc.dataset_readers.qangaroo import QangarooReader
from allennlp_rc.dataset_readers.quac import QuACReader
from allennlp_rc.dataset_readers.squad import SquadReader
from allennlp_rc.dataset_readers.triviaqa import TriviaQaReader