import random
import string

import pandas
from tqdm import tqdm

from lookout.style.typos.utils import Columns


letters = list(string.ascii_lowercase)


def rand_insert(token: str) -> str:
    """
    Add random letter inside a token.
    """
    letter = random.choice(letters)
    if len(token) == 0:
        return letter
    pos = random.choice(range(len(token) + 1))
    if pos == len(token):
        return token + letter
    return token[:pos] + letter + token[pos:]


def rand_delete(token: str) -> str:
    """
    Delete random symbol from a token.
    """
    if len(token) == 0:
        return token
    pos = random.choice(range(len(token)))
    return token[:pos] + token[pos + 1:]


def rand_substitution(token: str) -> str:
    """
    Substitute random symbol with a letter inside a token.
    """
    if len(token) == 0:
        return token
    pos = random.choice(range(len(token)))
    return token[:pos] + random.choice([c for c in letters if c != token[pos]]) + token[pos + 1:]


def rand_swap(token: str) -> str:
    """
    Swap two random consequent symbols.
    """
    if len(token) < 2 or len(set(token)) == 1:
        return token
    pos = random.choice(range(len(token) - 1))
    while token[pos] == token[pos + 1]:
        pos = random.choice(range(len(token) - 1))
    return token[:pos] + token[pos + 1] + token[pos] + token[pos + 2:]


def rand_typo(token: str) -> str:
    """
    Make random typo in a token.
    """
    return random.choice([rand_insert, rand_delete, rand_substitution, rand_swap])(token)


def corrupt_tokens_in_df(data: pandas.DataFrame, typo_probability: float,
                         add_typo_probability: float) -> pandas.DataFrame:
    """
    Create artificial typos in tokens from a dataframe. \
    Augment some of identifiers from dataframe with "typo_probability", \
    consequent typos in the same word happen with "add_typo_probability" each. \
    Operations happens out-of-place.

    :param data: Dataframe which contains columns Columns.Token and Columns.Split.
    :param typo_probability: Probability with which a token gets to be corrupted.
    :param add_typo_probability: Probability with which one more corruption happens to a \
                                 corrupted token.
    :return: New dataframe with added columns Columns.CorrectToken and Columns.CorrectSplit, \
             which contain tokens and corresponding splits from the `data`. Columns.Token and \
             Columns.Split now contain partially corrupted tokens and corresponding splits.
    """
    result = data.copy()
    result.loc[:, Columns.CorrectToken] = data[Columns.Token]
    result.loc[:, Columns.CorrectSplit] = data[Columns.Split]
    for i in tqdm(range(len(data))):
        token = data.iloc[i][Columns.Token]
        typoed_token = token
        if len(token) > 1 and random.uniform(0, 1) < typo_probability:
            typoed_token = ""
            while len(typoed_token) < 2:
                typoed_token = rand_typo(token)
                while random.uniform(0, 1) < add_typo_probability:
                    typoed_token = rand_typo(typoed_token)
        result.iloc[i][Columns.Split] = data.iloc[i][Columns.Split].replace(token, typoed_token)
        result.iloc[i][Columns.Token] = typoed_token
    return result
