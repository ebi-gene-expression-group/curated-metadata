import codecs
from collections import defaultdict
import sys

def check_for_mapping_conflict():
    """This test checks if a single term has been mapped two more than one
    ontology terms"""
    with codecs.open(sys.argv[1], encoding='utf-8') as f:
        term_dict = defaultdict(set)
        header = f.readline()
        for line in f:
            values = [value.strip() for value in line.split('\t')]
            category, term, ontology_ref, study, assay, annotator, date = values
            term_dict[term].add(ontology_ref)

        conflicts = [(t, url) for t, url in term_dict.items() if len(term_dict[t]) > 1]
        if conflicts:
            for mapping in conflicts:
                print("{} has been mapped to multiple terms:\t{}".format(mapping[0],
                 ', '.join(mapping[1])))

            sys.exit(1)


if __name__ == '__main__':
    check_for_mapping_conflict()
