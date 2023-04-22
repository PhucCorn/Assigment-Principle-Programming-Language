from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        if ctx.decllist():
            return Program(self.visit(ctx.decllist()))
        return Program([])

    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        return self.visit(ctx.decl()) + self.visit(ctx.decltail())
    
    def visitDecltail(self, ctx: MT22Parser.DecltailContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.decl()) + self.visit(ctx.decltail())
    
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.getChildCount() != 1:
            idlist = self.visit(ctx.idlist())
            atyp = self.visit(ctx.atyp())
            return list(map(lambda x: VarDecl(x,atyp), idlist))
        return self.visit(ctx.initiazation())
    
    def visitInitiazation(self, ctx: MT22Parser.InitiazationContext):
        listID = self.visit(ctx.initcy())
        last = listID[-1]
        atyp = last[-1]
        return list(map(lambda x: VarDecl(listID[x][0],atyp,listID[-1-x][1]), range(len(listID))))
    
    def visitInitcy(self, ctx: MT22Parser.InitcyContext):
        if ctx.atyp():
            return [[ctx.ID().getText(),self.visit(ctx.val()),self.visit(ctx.atyp())]]
        return [[ctx.ID().getText(),self.visit(ctx.val())]] + self.visit(ctx.initcy())
    
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        id = ctx.ID(0).getText()
        typ = self.visit(ctx.typ())
        paramlist = self.visit(ctx.paramlist())
        body = self.visit(ctx.body())
        if ctx.INHERIT():
            return [FuncDecl(id,typ,paramlist,ctx.ID(1).getText(),body)]
        return [FuncDecl(id,typ,paramlist,None,body)]
    
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
    
    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
        elif ctx.getChildCount() == 2:
            return [self.visit(ctx.param())]
        return []
    
    def visitParam(self, ctx: MT22Parser.ParamContext):
        inherit = False
        out = False
        id = ctx.ID().getText()
        atyp = self.visit(ctx.atyp())
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True
        return ParamDecl(id,atyp,out,inherit)
    
    def visitBody(self, ctx: MT22Parser.BodyContext):
        return self.visit(ctx.blockstmt())
    
    def visitTstmt(self, ctx: MT22Parser.TstmtContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        return self.visit(ctx.blockstmt())
    
    def visitFstmt(self, ctx: MT22Parser.FstmtContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        return self.visit(ctx.blockstmt())
    
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        if ctx.stmtlist():
            return BlockStmt(self.visit(ctx.stmtlist()))
        return BlockStmt([])
    
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        if ctx.getChildCount() == 1:
            if ctx.stmt():
                return [self.visit(ctx.stmt())]
            return self.visit(ctx.vardecl())
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.stmtlist())
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
    
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.asstmt():
            return self.visit(ctx.asstmt()) 
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt()) 
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt()) 
        elif ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt()) 
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt()) 
        elif ctx.contstmt():
            return self.visit(ctx.contstmt()) 
        return self.visit(ctx.retstmt()) 
    
    def visitAsstmt(self, ctx: MT22Parser.AsstmtContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs,rhs)
    
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.indexop())
    
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.tstmt()) 
        fstmt = None
        if ctx.ELSE():
            fstmt = self.visit(ctx.fstmt())
        return IfStmt(cond,tstmt,fstmt)
    
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        init = AssignStmt(self.visit(ctx.lhs()),self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = None
        if ctx.blockstmt():
            stmt = self.visit(ctx.blockstmt())
        else: 
            stmt = self.visit(ctx.stmt())
        return ForStmt(init,cond,upd,stmt)
    
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        expr = self.visit(ctx.expr())
        stmt = None
        if ctx.blockstmt():
            stmt = self.visit(ctx.blockstmt())
        else: 
            stmt = self.visit(ctx.stmt())
        return WhileStmt(expr,stmt)
    
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(expr,stmt)
    
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()
    
    def visitContstmt(self, ctx: MT22Parser.ContstmtContext):
        return ContinueStmt()
    
    def visitRetstmt(self, ctx: MT22Parser.RetstmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())  
        return ReturnStmt(expr)
    
    def visitCallstmt(self, ctx: MT22Parser.ProgramContext):
        id = None
        if ctx.ID():
            id = ctx.ID().getText()
        else:
            id = ctx.SPECIAL_FUNC().getText()
        args = []
        if ctx.arglist():
            args = self.visit(ctx.arglist())
        return CallStmt(id,args)
    
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())
        return [self.visit(ctx.expr())]
    
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.getChildCount != 2:
            return []
        return [self.visit(ctx.expr())]
    
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.string():
            return self.visit(ctx.string())
        return self.visit(ctx.funccall())
    
    def visitString(self, ctx: MT22Parser.StringContext):
        if ctx.getChildCount() == 3:
            op = ctx.DOUBLECOLON().getText()
            left = self.visit(ctx.relational(0))
            right = self.visit(ctx.relational(1))
            return BinExpr(op,left,right)
        return self.visit(ctx.relational(0))
    
    def visitRelational(self, ctx: MT22Parser.RelationalContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.logical(0))
            right = self.visit(ctx.logical(1))
            op = None
            if ctx.EQUAL():
                op = ctx.EQUAL().getText()
            elif ctx.DIF():
                op = ctx.DIF().getText()
            elif ctx.SMALLER():
                op = ctx.SMALLER().getText()
            elif ctx.BIGGER():
                op = ctx.BIGGER().getText()
            elif ctx.SMALLER_OR_EQUAL():
                op = ctx.SMALLER_OR_EQUAL().getText()
            elif ctx.BIGGER_OR_EQUAL():
                op = ctx.BIGGER_OR_EQUAL().getText()
            return BinExpr(op,left,right)
        if ctx.logical():
            return self.visit(ctx.logical(0))
        return StringLit(ctx.STR().getText())
    
    def visitLogical(self, ctx: MT22Parser.LogicalContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.logical())
            right = self.visit(ctx.adding())
            op = None
            if ctx.AND():
                op = ctx.AND().getText()
            else:
                op = ctx.OR().getText()
            return BinExpr(op,left,right)
        return self.visit(ctx.adding())
    
    def visitAdding(self, ctx: MT22Parser.AddingContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.adding())
            right = self.visit(ctx.multiplying())
            op = None
            if ctx.ADD():
                op = ctx.ADD().getText()
            else:
                op = ctx.MINUS().getText()
            return BinExpr(op,left,right)
        return self.visit(ctx.multiplying())
    
    def visitMultiplying(self, ctx: MT22Parser.MultiplyingContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.multiplying())
            right = self.visit(ctx.not_logical())
            op = None
            if ctx.MUL():
                op = ctx.MUL().getText()
            else:
                op = ctx.DIV().getText()
            return BinExpr(op,left,right)
        elif ctx.getChildCount == 2:
            val = self.visit(ctx.multiplying())
            op = ctx.PER().getText()
            return UnExpr(op,val)
        return self.visit(ctx.not_logical())
    
    def visitNot_logical(self, ctx: MT22Parser.Not_logicalContext):
        if ctx.getChildCount() == 1:
            if ctx.sign():
                return self.visit(ctx.sign())
            elif ctx.TRUE():
                return BooleanLit(ctx.TRUE().getText())
            return BooleanLit(ctx.FALSE().getText())
        val = self.visit(ctx.not_logical())
        op = ctx.NOT().getText()
        return UnExpr(op,val)
    
    def visitSign(self, ctx: MT22Parser.SignContext):
        if ctx.indexop():
            return self.visit(ctx.indexop())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INT():
            return IntegerLit(ctx.INT())
        elif ctx.FL():
            return FloatLit(ctx.FL())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        val = self.visit(ctx.sign())
        op = ctx.MINUS().getText()
        return UnExpr(op,val)
    
    def visitIndexop(self, ctx: MT22Parser.IndexopContext):
        name = ctx.ID().getText()
        cell = self.visit(ctx.exprlist())
        return ArrayCell(name,cell)
    
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        id = ctx.ID().getText()
        args = []
        if ctx.arglist():
            args = self.visit(ctx.arglist())
        return FuncCall(id,args)
    
    def visitArglist(self, ctx: MT22Parser.ArglistContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.arg())] + self.visit(ctx.arglist())
        return [self.visit(ctx.arg())]
    
    def visitArg(self, ctx: MT22Parser.ProgramContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.expr())
    
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.vartype())
    
    def visitVal(self, ctx: MT22Parser.ValContext):
        if ctx.INT():
            return IntegerLit(ctx.INT())
        elif ctx.FL():
            return FloatLit(ctx.FL())
        elif ctx.TRUE():
            return BooleanLit(ctx.TRUE())
        elif ctx.FALSE():
            return BooleanLit(ctx.FALSE())
        elif ctx.STR():
            return StringLit(ctx.STR())
        elif ctx.ARR():
            d = ctx.ARR().getText()
            strlist = d[1:-1].split(",")
            intlist = [eval(i) for i in strlist]
            #Có thể mỗi phần tử trong strlist không phải là số 
            return ArrayLit(intlist)
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        return self.visit(ctx.expr())
    
    def visitVartype(self, ctx: MT22Parser.VartypeContext):
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.atyp())
    
    def visitAtyp(self, ctx: MT22Parser.AtypContext):
        if ctx.fourarrtype():
            return self.visit(ctx.fourarrtype())
        return self.visit(ctx.arraytype())
    
    def visitFourarrtype(self, ctx: MT22Parser.FourarrtypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        return StringType()
    
    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        dimensions = self.visit(ctx.dimensionlist())
        type = self.visit(ctx.fourarrtype())
        return ArrayType(dimensions,type)
    
    def visitDimensionlist(self, ctx: MT22Parser.DimensionlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.INT().getText()]
        return [ctx.INT().getText()] + self.visit(ctx.dimensionlist())
    
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())