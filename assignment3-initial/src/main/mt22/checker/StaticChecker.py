from Visitor import Visitor
from functools import reduce

class Var:
    #(ast.name,ast.typ,'variable')
    def __init__(self, name, typ, ar_typ = None):
        self.name = name
        self.typ = typ
        self.ar_typ = ar_typ

class Func:
    #ast.name,ast.return_type,ast.inherit,in_func[1]+in_func[0],'function'
    def __init__(self, name, return_type, inherit, in_func):
        self.name = name
        self.return_type = return_type
        self.inherit = inherit
        self.in_func = in_func

class Para:
    #ast.name,ast.typ,ast.inherit,'parameter'
    def __init__(self, name, typ, inherit):
        self.name = name
        self.typ = typ
        self.inherit = inherit

class Utils:
    def infer(param_list, name, typ):
        for param in param_list:
            if param.name == name:
                param.return_type = typ
                return typ

    def typ_ar(list):
        if type(list) is type([]):
            return typ_ar(list[0])
        return list.typ

class StaticChecker(Visitor):
    def visitIntegerType(self, ast, param): return IntegerType()

    def visitFloatType(self, ast, param): return FloatType()

    def visitBooleanType(self, ast, param): return BooleanType()

    def visitStringType(self, ast, param): return StringType()

    def visitArrayType(self, ast, param): return ArrayType()

    def visitAutoType(self, ast, param): return AutoType()

    def visitVoidType(self, ast, param): return VoidType()

    def visitBinExpr(self, ast, param): 
        left = self.visit(ast.left,[param[0],param[1],None])
        right = self.visit(ast.right,[param[0],param[1],None])
        if ast.op in ['+','-','*','/','<','>','<=','>=']:
            if type(left) is AutoType and type(right) is AutoType and type(param[-1]) is None:
                return AutoType()
            if type(left) is AutoType and type(right) is AutoType and type(param[-1]) is not None:
                if type(param[-1]) in [IntegerType, FloatType]:
                    left = self.visit(ast.left,param)
                    right = self.visit(ast.right,param)
                    return right
                return IntegerType()
            if type(right) not in [IntegerType, FloatType, AutoType] or type(left) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is AutoType:
                #Utils.infer(param[2],ast.left.name,right)
                self.visit(ast.left,param)
                return right
            if type(right) is AutoType:
                # Utils.infer(param[2],ast.right.name,left)
                left = self.visit(ast.right,param)
                return left
            if ast.op == '/':
                return FloatType()
            if type(right) is FloatType or type(left) is FloatType:
                return FloatType()
            return IntegerType()
        if ast.op in ['%']:
            if type(right) not in [IntegerType, AutoType] or type(left) not in [IntegerType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is AutoType:
                #Utils.infer(param[2],ast.left.name,IntegerType())
                self.visit(ast.left,[param[0],param[1],IntegerType()])
                return IntegerType()
            if type(right) is AutoType:
                #Utils.infer(param[2],ast.right.name,IntegerType())
                self.visit(ast.right,[param[0],param[1],IntegerType()])
                return IntegerType()
            return IntegerType()
        if ast.op in [':']:
            if type(right) not in [StringType, AutoType] or type(left) not in [StringType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is AutoType:
                #Utils.infer(param[2],ast.left.name,StringType())
                self.visit(ast.left,[param[0],param[1],StringType()])
                return right
            if type(right) is AutoType:
                #Utils.infer(param[2],ast.right.name,StringType())
                self.visit(ast.right,[param[0],param[1],StringType()])
                return left
            return StringType()
        if ast.op in ['==','!=']:
            if type(left) is AutoType and type(right) is AutoType and type(param[-1]) is None:
                return AutoType()
            if type(left) is AutoType and type(right) is AutoType and type(param[-1]) is not None:
                left = self.visit(ast.left,param)
                right = self.visit(ast.right,param)
            if type(right) not in [IntegerType, BooleanType, AutoType] or type(left) not in [IntegerType, BooleanType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is AutoType:
                #Utils.infer(param[2],ast.left.name,right)
                self.visit(ast.left,param)
                return right
            if type(right) is AutoType:
                #Utils.infer(param[2],ast.right.name,left)
                self.visit(ast.right,param)
                return left
            if type(right) is type(left):
                if type(right) is BooleanType:
                    return BooleanType()
                if type(right) is IntegerType:
                    return IntegerType()
            raise TypeMismatchInExpression(ast)
        if ast.op in ['&&','||']:
            if type(right) not in [BooleanType, AutoType] or type(left) not in [BooleanType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is AutoType:
                #Utils.infer(param[2],ast.left.name,BooleanType())
                self.visit(ast.left,[param[0],param[1],BooleanType()])
                return BooleanType()
            if type(right) is AutoType:
                #Utils.infer(param[2],ast.right.name,BooleanType())
                self.visit(ast.right,[param[0],param[1],BooleanType()])
                return BooleanType()
            return BooleanType()
        raise TypeMismatchInExpression(ast)

        # if ast.op in ['+','-','*','/','<','>','<=','>=']:
        #     if type(right) not in [IntegerType, FloatType] or type(left) not in [IntegerType, FloatType]:
        #         raise TypeMismatchInExpression(ast)
        #     if ast.op == '/':
        #         return FloatType()
        #     if type(right) is FloatType or type(left) is FloatType:
        #         return FloatType()
        #     return IntegerType()
        # if ast.op in ['%']:
        #     if type(right) not in [IntegerType] or type(left) not in [IntegerType]:
        #         raise TypeMismatchInExpression(ast)
        #     return IntegerType()
        # if ast.op in [':']:
        #     if type(right) not in [StringType] or type(left) not in [StringType]:
        #         raise TypeMismatchInExpression(ast)
        #     return StringType()
        # if ast.op in ['==','!=']:
        #     if type(right) not in [IntegerType, BooleanType] or type(left) not in [IntegerType, BooleanType]:
        #         raise TypeMismatchInExpression(ast)
        #     if type(right) is type(left):
        #         if type(right) is BooleanType:
        #             return BooleanType()
        #         if type(right) is IntegerType:
        #             return IntegerType()
        #     raise TypeMismatchInExpression(ast)
        # if ast.op in ['&&','||']:
        #     if type(right) not in [BooleanType] or type(left) not in [BooleanType]:
        #         raise TypeMismatchInExpression(ast)
        #     return BooleanType()

    def visitUnExpr(self, ast, param):
        val = self.visit(ast.val,[param[0],param[1],None])
        if ast.op == '-':
            if type(val) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(val) is AutoType:
                if not param[2]:
                    return AutoType()
                if type(param[2]) in [IntegerType, FloatType]:
                    #Utils.infer(param,val.name,param[2])
                    self.visit(ast.val,param)
                    return param[2]
                return IntegerType() #return Int hay Float đều được
            return val
        elif ast.op == '!':
            if type(val) not in [BooleanType, AutoType]:
                raise TypeMismatchInExpression(ast)
            if type(val) is AutoType:
                #Utils.infer(param,val.name,param[2])
                self.visit(ast.val,[param[0],param[1],BooeanType()])
            return BooleanType()
        raise TypeMismatchInExpression(ast)

    def visitId(self, ast, param):
        for param_list in param[:-1]:
            for decl in param_list:
                if decl.name == ast.name:
                    return decl.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, param): 
        typ = self.visit(ast.name,param)
        if type(typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for cell in ast.cell:
            if type(self.visit(cell,param)) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        return typ.typ
    
    def visitIntegerLit(self, ast, param): return IntegerType()

    def visitFloatLit(self, ast, param): return FloatType()

    def visitStringLit(self, ast, param): return StringType()

    def visitBooleanLit(self, ast, param): return BooleanType()

    def visitArrayLit(self, ast, param):
        if ast.explist == []:
            return ArrayType([0],typ = None)
        t = type(self.visit(ast.explist[0],param))
        for expr in ast.explist[1:]:
            if t is not type(self.visit(expr,param)):
                raise IllegalArrayLiteral(ast)
        return ArrayType([0],typ = t)

    def visitFuncCall(self, ast, param):
        func = None
        for decl in param[-2]:
            if ast.name == decl.name and type(decl) == Func:
              func = decl
              break
        if not func:
            raise Undeclared(Function(), ast.name)  
        if type(func.return_type) is VoidType:
            raise TypeMismatchInExpression(ast)
        for arg in range(ctx.args):
            if type(self.visit(ctx.args[arg],param)) is not type(func.in_func[arg].typ):
                raise TypeMismatchInStatement(ast)
        if type(func.return_type) is AutoType and param[-1]:
            Utils.infer(param,ast.name,param[2])
        return func.return_type

    def visitAssignStmt(self, ast, param):
        rhs = self.visit(ast.rhs,[param[2],param[3],None])
        lhs = self.visit(ast.lhs,[param[2],param[3],None])
        if type(lhs) is VoidType or type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(rhs) is AutoType and type(lhs) is AutoType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType:
            #Utils.infer(param[2],ast.lhs.name,rhs)
            self.visit(ast.lhs,[param[2],param[3],rhs])
            return param #Change type of lhs same with rhs
        if type(rhs) is AutoType:
            #Utils.infer(param[2],ast.rhs.name,lhs)
            self.visit(ast.rhs,[param[2],param[3],lhs])
            return param
        if type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)
        return param

    def visitBlockStmt(self, ast, param):
        for stmt in ast.body:
            if stmt is VarDecl:
                self.visit(stmt,[param[2],param[3],None])
                continue
            self.visit(stmt,param)
        return param

    def visitIfStmt(self, ast, param): 
        if type(self.visit(ast.cond,[param[2],param[3],None])) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        reduce(lambda pre,cur: self.visit(cur,pre), [ast.tstmt]+[ast.fstmt], param)

    def visitForStmt(self, ast, param): 
        if type(self.visit(ast.init,param)) is not IntegerType and type(self.visit(ast.upd,[param[2],param[3],None])) is not IntegerType: #AssignStmt and exp must return type
            raise TypeMismatchInStatement(ast)
        if type(self.visit(ast.cond,[param[2],param[3],None])) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        param[1] = True
        self.visit(ast.stmt,param)
        return param

    def visitWhileStmt(self, ast, param): 
        if type(self.visit(ast.cond,[param[2],param[3],None])) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        param[1] = True
        self.visit(ast.stmt,param)
        return param

    def visitDoWhileStmt(self, ast, param): 
        if type(self.visit(ast.cond,param)) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        param[1] = True
        self.visit(ast.stmt,param)
        return param
        
    def visitBreakStmt(self, ast, param): 
        if param[1] is False:
            raise MustInLoop(ast)
        return param

    def visitContinueStmt(self, ast, param): 
        if param[1] is False:
            raise MustInLoop(ast)
        return param

    def visitReturnStmt(self, ast, param): 
        if type(self.visit(ast.expr,[param[2],param[3],None])) != type(param[0]):
            raise TypeMismatchInStatement(ast)
        return param

    def visitCallStmt(self, ast, param): 
        func = None
        for decl in param[-1]:
            if decl.name == ast.name and type(decl) is Func:
                func = decl
                break
        if not func: raise Undeclared(Function(), ast.name)
        for i in range(ast.args):
            if type(self.visit(ast.args[i],[param[2],param[3],None])) is not type(func.in_func[i].typ):
                raise TypeMismatchInStatement(ast) 
        return param

    def visitVarDecl(self, ast, param): 
        for decl in param[0]:
            if decl.name == ast.name:
                raise Redeclared(Variable(),ast.name)
        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(),ast.name)
        if ast.init:
            typ = self.visit(ast.init,param)
            if type(ast.typ) is AutoType:
                if type(typ) is not ArrayType:
                    param[0] += [Var(ast.name,typ)]
                    return param
                else:
                    param[0] += [Var(ast.name,typ,typ.typ)]
                    return param
            if type(ast.typ) is FloatType and type(typ) is IntegerType:
                param[0] += [Var(ast.name,FloatType())]
                return param
            if type(ast.typ) is not type(typ):
                raise TypeMismatchInStatement(ast)
        if type(typ) is not ArrayType:
            param[0] += [Var(ast.name,ast.typ)]
            return param
        else:
            param[0] += [Var(ast.name,ast.typ,ast.typ.typ)]
            return param
            
    def visitParamDecl(self, ast, param): 
        for decl in param[0]: #param[0] is local param, param[1] is inherit param
            if decl.name == ast.name:
                raise Redeclared(Parameter(),ast.name)
        for decl in param[1]:
            if decl.name == ast.name:
                raise Invalid(Parameter(),ast.name)
        param[0] += [Para(ast.name,ast.typ,ast.inherit)]
        return param
        

    def visitFuncDecl(self, ast, param): 
        for decl in param[0]:
            if decl.name == ast.name:
                raise Redeclared(Function(),ast.name)
        if ast.name == 'main' and (type(ast.return_type) is not VoidType or ast.params != []):
            raise NoEntryPoint()
        param[0] += [Func(ast.name,ast.return_type,ast.inherit,[])]
        out_func = param[0]
        param_func = []
        if ast.inherit:
            for decl in param[0]:
                if ast.inherit == decl.name:
                    for par in decl.in_func:
                        if par.inherit:
                            param_func += [par]
            raise Undeclared(Function(),ast.inherit) 
        in_func = reduce(lambda pre,cur: self.visit(cur,pre), ast.params, [[],param_func]) # param trong hàm và param inherit
        if ast.inherit:
            #check dòng đầu tiên(Đã làm)
            if decl.in_func is not []:
                if ast.body.body[0].name not in ['super','preventDefault']:
                    raise InvalidStatementInFunction('super')
        param[0][-1].in_func += in_func[1]+in_func[0]
        self.visit(ast.body,[ast.return_type,False,in_func[1]+in_func[0],out_func]) # return_type, cycle or not, in func, out func
        return param

    def visitProgram(self, ast, param): 
        param = [[]]
        param[0] += [Func('readInteger',IntegerType(),None,[])]
        param[0] += [Func('printInteger',VoidType(),None,[Para('anArg',IntegerType(),False)])]
        param[0] += [Func('readFloat',FloatType(),None,[])]
        param[0] += [Func('writeFloat',VoidType(),None,[Para('anArg',FloatType(),False)])]
        param[0] += [Func('readBoolean',BooleanType(),None,[])]
        param[0] += [Func('printBoolean',VoidType(),None,[Para('anArg',BooleanType(),False)])]
        param[0] += [Func('readString',StringType(),None,[])]
        param[0] += [Func('printString',VoidType(),None,[Para('anArg',StringType(),False)])]
        param[0] += [Func('preventDefault',VoidType(),None,[])]
        reduce(lambda pre,cur: self.visit(cur,pre), ast.decls, param)
