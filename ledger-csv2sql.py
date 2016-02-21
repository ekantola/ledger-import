#! /usr/bin/env python3

import sys
import csv

BANK_ACCOUNT_ID=10011

for row in csv.reader(sys.stdin):
  reference, transdate, person, description, amount, account_no = row
  print("""\
INSERT INTO gl (id, reference, transdate, description, notes) VALUES (DEFAULT, '{reference}', '{transdate}', '{description}', '{person}');
INSERT INTO acc_trans (trans_id, chart_id, amount, transdate, source) VALUES ((SELECT last_value FROM id), (SELECT id FROM chart WHERE accno='{other_account}'), {amount}, '{transdate}', '{reference}');
INSERT INTO acc_trans (trans_id, chart_id, amount, transdate, source) VALUES ((SELECT last_value FROM id), {bank_account_chart_id}, -({amount}), '{transdate}', '{reference}');
""".format(reference=reference, transdate=transdate, person=person, description=description, amount=amount, other_account=account_no, bank_account_chart_id=BANK_ACCOUNT_ID))
