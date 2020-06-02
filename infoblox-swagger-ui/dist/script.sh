#!/bin/sh

#Author: Vedant Sethia 
#Copyright (c) infoblox.com

cp $1/dns.json dns.json
cp $1/dhcp.json dhcp.json
cp $1/ipam.json ipam.json
cp $1/dtc.json dtc.json
cp $1/grid.json grid.json
cp $1/rpz.json rpz.json
cp $1/parental_control.json parental_control.json
cp $1/discovery.json discovery.json
cp $1/microsoft.json microsoft.json
cp $1/outbound.json outbound.json
cp $1/users.json users.json
cp $1/threat_analytics.json threat_analytics.json
cp $1/miscellaneous.json miscellaneous.json
cp $1/vlan.json vlan.json

python variable.py $2 
