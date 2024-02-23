#!/bin/bash

zmprov -l gaa > /tmp/contas

cat /tmp/contas  | while read CONTAS ; do echo ga $CONTAS zimbraLastLogonTimestamp ; done > /tmp/EXEC

zmprov -f /tmp/EXEC > /tmp/FINAL

cat /tmp/FINAL | grep name | awk '{print $4}' | while read ACC ; do echo "$ACC;`cat /tmp/FINAL | grep -A1 $ACC | grep zimbraLastLogonTimestamp | awk '{print $2}' | sed 's/.[0-9][0-9][0-9]Z//g'`" >> /tmp/accslastlogon_temp; done
