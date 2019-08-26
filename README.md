# qo100-groundstation
Software for the QO-100 groundstation of EA4GPZ

This repository contains software that I use in my QO-100 (Eshail-2)
groundstation. The groundstation constists of a BeagleBone Black driving a
LimeSDR mini which is connected to a Ku-band LNB for the downlink and a large
2.4GHz PA for the uplink. More information about the groundstation can be seen
[here](https://www.crowdsupply.com/lime-micro/limesdr-mini/updates/field-report-limesdr-mini-satellite-ground-station).

## Narrowband transponder software

### Linrad and GNU Radio streaming software

My main software solution for the narrowband transponder uses an external
computer running [Linrad](http://www.sm5bsz.com/linuxdsp/linrad.htm) for RX and
GNU Radio for TX.

To run this software you must:

1. Start the Linrad Python server `linrad_server.py`
2. Start the socat server that will listen to GNU Radio using
`start_gnuradio_socat`
3. Start the LimeSDR streamer using `start_eshail_limesdr`

In another PC you can use `eshail_300k.grc` to stream TX samples using GNU Radio
and Linrad using the network protocol (16bit RAW samples IP 239.255.0.0) to
receive the downlink.

