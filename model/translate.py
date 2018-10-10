#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
import argparse

from onmt.utils.logging import init_logger
from onmt.translate.translator import build_translator

import onmt.inputters
import onmt.translate
import onmt
import onmt.model_builder
import onmt.modules
import onmt.opts


def main(opt):
    # Is this where weights are loaded? I Think it's here. So do this ahead of time.
    translator = build_translator(opt, report_score=True)
    # Or is this?
    translator.translate(src_path=opt.src,
                         tgt_path=opt.tgt,
                         src_dir=opt.src_dir,
                         batch_size=opt.batch_size,
                         attn_debug=opt.attn_debug)


if __name__ == "__main__":
    # When translate.py is called, first parse all the arguments.
    # This stuff doesn't change. Things like beam_size etc. But even the src is always fwd-tok.txt. The content
    # will change but the filename doesn't. So this could be done ahead of time. Definitely not the major bottleneck
    # though.
    parser = argparse.ArgumentParser(
        description='translate.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    onmt.opts.add_md_help_argument(parser)
    onmt.opts.translate_opts(parser)
    opt = parser.parse_args()
    logger = init_logger(opt.log_file) # Output logger
    
    main(opt)

## Proto
