# -*- coding: utf-8 -*-
import log
import traceback


class ExceptionUtils:
    @classmethod
    def exception_traceback(cls, e):
        log.info(f"\nException: {str(e)}\nCallstack:\n{traceback.format_exc()}\n")
