# FlowUI terminal interface
#
# Copyright (c) 2012-2013, David Holm <dholmster@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author of FlowUI nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL DAVID HOLM BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


class Terminal(object):
    DEFAULT_WIDTH = 80
    DEFAULT_HEIGHT = 25
    DEFAULT_DEPTH = 8

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT,
                 depth=DEFAULT_DEPTH):
        self._width = width
        self._height = height
        self._depth = depth

    def write(self, string, dictionary=None):
        raise NotImplementedError()

    def len(self, string, dictionary=None):
        if dictionary is not None:
            string = string.format(dictionary)
        len(string)

    def depth(self):
        return self._depth

    def width(self):
        return self._width

    def height(self):
        return self._height


class ThemedTerminal(Terminal):
    def __init__(self, terminal, theme):
        super(ThemedTerminal, self).__init__(terminal.width(),
                                             terminal.height(),
                                             terminal.depth())
        self._terminal = terminal
        self._theme = theme

    def len(self, string, dictionary=None):
        return self._theme.len(string, dictionary)

    def clear(self):
        self._terminal.write(self._theme.control('clear-screen'))

    def reset(self):
        self._terminal.write(self._theme.property('normal'))

    def write(self, string, dictionary=None):
        self._terminal.write(self._theme.write(string, dictionary))
