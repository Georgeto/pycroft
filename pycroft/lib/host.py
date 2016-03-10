# -*- coding: utf-8 -*-
# Copyright (c) 2015 The Pycroft Authors. See the AUTHORS file.
# This file is part of the Pycroft project and licensed under the terms of
# the Apache License, Version 2.0. See the LICENSE file for details.
from pycroft.helpers.i18n import deferred_gettext
from pycroft.lib.logging import log_user_event
from pycroft.model.session import with_transaction


@with_transaction
def change_mac(net_device, mac, processor):
    """
    This method will change the mac address of the given net device to the new
    mac address.

    :param net_device: the net device which should become a new mac address.
    :param mac: the new mac address.
    :param processor: the user who initiated the mac address change.
    :return: the changed net device with the new mac address.
    """
    old_mac = net_device.mac
    net_device.mac = mac
    message = deferred_gettext(u"Changed MAC address from {} to {}.").format(
        old_mac, mac)
    log_user_event(message.to_json(), processor, net_device.host.user)
    return net_device


def generate_hostname(ip_address):
    return "whdd" + ip_address.split(u".")[-1]
