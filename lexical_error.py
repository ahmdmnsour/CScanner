class LexicalError:
    class ErrorCode:
        CannotOpenFile, AboveIDLimit, SingleAmpersand, SingleBar, InvalidChar, InvalidComment = range(6)

    @staticmethod
    def get_error_message(code):
        msg = f"Lexical Error(code: {code})\n"
        if code == LexicalError.ErrorCode.CannotOpenFile:
            msg += "cannot open the file. please check the file path."
        elif code == LexicalError.ErrorCode.AboveIDLimit:
            msg += "an identifier length must be less than 12."
        elif code == LexicalError.ErrorCode.SingleAmpersand:
            msg += "next character must be &."
        elif code == LexicalError.ErrorCode.SingleBar:
            msg += "next character must be |."
        elif code == LexicalError.ErrorCode.InvalidChar:
            msg += "invalid character!!!"
        elif code == LexicalError.ErrorCode.InvalidComment:
            msg += "invalid block comment!"
        else:
            msg += "Unknown Error"
        return msg
