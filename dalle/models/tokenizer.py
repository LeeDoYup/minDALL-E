# ------------------------------------------------------------------------------------
# Minimal DALL-E
# Copyright (c) 2021 Kakao Brain Corp. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 [see LICENSE for details]
# ------------------------------------------------------------------------------------

import os
from functools import partial
from tokenizers import CharBPETokenizer


def build_tokenizer(path: str,
                    context_length: int = 64,
                    *args,
                    **kwargs):
    from_file = partial(CharBPETokenizer.from_file,
                        vocab_filename=os.path.join(path, 'bpe-16k-vocab.json'),
                        merges_filename=os.path.join(path, 'bpe-16k-merges.txt'),
                        unk_token='[UNK]')
    tokenizer = from_file(*args, **kwargs)
    tokenizer.add_special_tokens(['[PAD]'])
    tokenizer.enable_padding(length=context_length,
                             pad_id=tokenizer.token_to_id('[PAD]'))
    tokenizer.enable_truncation(max_length=context_length)
    print(f'{path} successfully restored..')
    return tokenizer
