#!/usr/bin/env python

import sys
import argparse
import json
import gzip

output = []


with open("../config/record.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)

# def main(path, out_file):
#     num_lines = 0
#     with gzip.open(path, 'rt') as fp:
#         for line in fp:
#             output.append("<DOC>")
#             doc = json.loads(line)
#             output.append("<DOCNO>" + doc["id"] + "</DOCNO>")
#             for key, value in doc.items():
#                 if key == "authors":
#                     names = []
#                     author_ids = []
#                     for author in value:
#                         names.append(author["name"] + "; ")
#                         for id in author["ids"]:
#                             author_ids.append(id)
#                     output.append("<AUTHORNAMES>")
#                     output.append(" ".join(names))
#                     output.append("</AUTHORNAMES>")
#                     output.append("<AUTHORIDS>")
#                     output.append(" ".join(author_ids))
#                     output.append("</AUTHORIDS>")
# 
#                 if key == "entities" or key == "outCitations" or key == "inCitations" or key == "pdfUrls" or \
#                                 key == "sources":
#                     values = " ".join(value)
#                     output.append("<" + key.upper() + ">")
#                     output.append(values)
#                     output.append("</" + key.upper() + ">")
# 
#                 if key == "year" or key == "venue" or key == "title" or key == "s2Url" or key == "s2PdfUrl" or \
#                                 key == "pmid" or key == "paperAbstract" or key == "journalVolume" or \
#                                 key == "journalPages" or key == "journalName" or key == "doiUrl" or key == "doi":
#                     output.append("<" + key.upper() + ">")
#                     output.append(str(value).strip())
#                     output.append("</" + key.upper() + ">")
# 
# 
#             output.append("</DOC>")
#             num_lines += 1
#             sys.stderr.write("Processed " + str(num_lines))
#         
#     
#     with gzip.open(out_file, 'wt') as o:
#         for line in output:
#             if line != "":
#                 o.write(line + "\n")




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert Fair Ranking 20 Semantic Scholar S2 corpus json to trecdocs")
    parser.add_argument("file_path", help="Path corpus-subset-for-queries.jsonl.")
    parser.add_argument("out_file", help="File to write the trecdocs to. File name should end .gz")
    args = parser.parse_args()

    p = args.file_path
    o = args.out_file
    main(p, o)
