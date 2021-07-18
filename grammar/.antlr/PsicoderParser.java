// Generated from c:\Users\USER\Documents\LP-2021-1\TraductorPsicoder\tradPsicoder\grammar\Psicoder.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PsicoderParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, COMMENT=33, LINE_COMMENT=34, WS=35, PIZQ=36, PDER=37, NEG=38, 
		ROI=39, ROP=40, ROL=41, SMCOLON=42, COMA=43, MULOP=44, SUMOP=45, DOUBLE=46, 
		INT=47, STRING=48, BOOLEANO=49, CONST=50, ID=51;
	public static final int
		RULE_s = 0, RULE_funcion_principal = 1, RULE_funcion = 2, RULE_retornar = 3, 
		RULE_parametros = 4, RULE_estructura = 5, RULE_declaracion = 6, RULE_asignacion = 7, 
		RULE_comandos = 8, RULE_comando = 9, RULE_si = 10, RULE_si_no = 11, RULE_para = 12, 
		RULE_asignacion_entero = 13, RULE_hacer_mientras = 14, RULE_mientras = 15, 
		RULE_seleccionar = 16, RULE_casos = 17, RULE_caso = 18, RULE_asignacion_id = 19, 
		RULE_leer = 20, RULE_imprimir = 21, RULE_romper = 22, RULE_llamar_funcion = 23, 
		RULE_pasar_parametros = 24, RULE_expresion_logica = 25, RULE_expresion_rop = 26, 
		RULE_expresion_roi = 27, RULE_expr = 28, RULE_tipo = 29, RULE_id_pos_estruct = 30;
	private static String[] makeRuleNames() {
		return new String[] {
			"s", "funcion_principal", "funcion", "retornar", "parametros", "estructura", 
			"declaracion", "asignacion", "comandos", "comando", "si", "si_no", "para", 
			"asignacion_entero", "hacer_mientras", "mientras", "seleccionar", "casos", 
			"caso", "asignacion_id", "leer", "imprimir", "romper", "llamar_funcion", 
			"pasar_parametros", "expresion_logica", "expresion_rop", "expresion_roi", 
			"expr", "tipo", "id_pos_estruct"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'funcion_principal'", "'fin_principal'", "'funcion'", "'hacer'", 
			"'fin_funcion'", "'retornar'", "'estructura'", "'fin_estructura'", "'='", 
			"'si'", "'entonces'", "'fin_si'", "'si_no'", "'para'", "'fin_para'", 
			"'entero'", "'mientras'", "'fin_mientras'", "'seleccionar'", "'entre'", 
			"'fin_seleccionar'", "'defecto'", "':'", "'caso'", "'leer'", "'imprimir'", 
			"'romper'", "'caracter'", "'cadena'", "'real'", "'booleano'", "'.'", 
			null, null, null, "'('", "')'", "'!'", null, null, null, "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "COMMENT", "LINE_COMMENT", 
			"WS", "PIZQ", "PDER", "NEG", "ROI", "ROP", "ROL", "SMCOLON", "COMA", 
			"MULOP", "SUMOP", "DOUBLE", "INT", "STRING", "BOOLEANO", "CONST", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Psicoder.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PsicoderParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class SContext extends ParserRuleContext {
		public Funcion_principalContext funcion_principal() {
			return getRuleContext(Funcion_principalContext.class,0);
		}
		public TerminalNode EOF() { return getToken(PsicoderParser.EOF, 0); }
		public List<FuncionContext> funcion() {
			return getRuleContexts(FuncionContext.class);
		}
		public FuncionContext funcion(int i) {
			return getRuleContext(FuncionContext.class,i);
		}
		public List<EstructuraContext> estructura() {
			return getRuleContexts(EstructuraContext.class);
		}
		public EstructuraContext estructura(int i) {
			return getRuleContext(EstructuraContext.class,i);
		}
		public SContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s; }
	}

	public final SContext s() throws RecognitionException {
		SContext _localctx = new SContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_s);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2 || _la==T__6) {
				{
				setState(64);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__2:
					{
					setState(62);
					funcion();
					}
					break;
				case T__6:
					{
					setState(63);
					estructura();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(69);
			funcion_principal();
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2 || _la==T__6) {
				{
				setState(72);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__2:
					{
					setState(70);
					funcion();
					}
					break;
				case T__6:
					{
					setState(71);
					estructura();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(77);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Funcion_principalContext extends ParserRuleContext {
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public Funcion_principalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion_principal; }
	}

	public final Funcion_principalContext funcion_principal() throws RecognitionException {
		Funcion_principalContext _localctx = new Funcion_principalContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_funcion_principal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__0);
			setState(80);
			comandos();
			setState(81);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncionContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(PsicoderParser.ID, 0); }
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public RetornarContext retornar() {
			return getRuleContext(RetornarContext.class,0);
		}
		public FuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion; }
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_funcion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(T__2);
			setState(84);
			tipo();
			setState(85);
			match(ID);
			setState(86);
			match(PIZQ);
			setState(87);
			parametros();
			setState(88);
			match(PDER);
			setState(89);
			match(T__3);
			setState(90);
			comandos();
			setState(91);
			retornar();
			setState(92);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RetornarContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SMCOLON() { return getToken(PsicoderParser.SMCOLON, 0); }
		public RetornarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retornar; }
	}

	public final RetornarContext retornar() throws RecognitionException {
		RetornarContext _localctx = new RetornarContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_retornar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__5);
			setState(95);
			expr(0);
			setState(96);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParametrosContext extends ParserRuleContext {
		public List<TipoContext> tipo() {
			return getRuleContexts(TipoContext.class);
		}
		public TipoContext tipo(int i) {
			return getRuleContext(TipoContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(PsicoderParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PsicoderParser.ID, i);
		}
		public List<TerminalNode> COMA() { return getTokens(PsicoderParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(PsicoderParser.COMA, i);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parametros);
		int _la;
		try {
			setState(110);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				tipo();
				setState(99);
				match(ID);
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMA) {
					{
					{
					setState(100);
					match(COMA);
					setState(101);
					tipo();
					setState(102);
					match(ID);
					}
					}
					setState(108);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case PDER:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EstructuraContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsicoderParser.ID, 0); }
		public List<DeclaracionContext> declaracion() {
			return getRuleContexts(DeclaracionContext.class);
		}
		public DeclaracionContext declaracion(int i) {
			return getRuleContext(DeclaracionContext.class,i);
		}
		public EstructuraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estructura; }
	}

	public final EstructuraContext estructura() throws RecognitionException {
		EstructuraContext _localctx = new EstructuraContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_estructura);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(T__6);
			setState(113);
			match(ID);
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__15) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << ID))) != 0)) {
				{
				{
				setState(114);
				declaracion();
				}
				}
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(120);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclaracionContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(PsicoderParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PsicoderParser.ID, i);
		}
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public TerminalNode SMCOLON() { return getToken(PsicoderParser.SMCOLON, 0); }
		public List<TerminalNode> COMA() { return getTokens(PsicoderParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(PsicoderParser.COMA, i);
		}
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_declaracion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			tipo();
			setState(123);
			match(ID);
			setState(124);
			asignacion();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(125);
				match(COMA);
				setState(126);
				match(ID);
				setState(127);
				asignacion();
				}
				}
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(133);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AsignacionContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_asignacion);
		try {
			setState(138);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				match(T__8);
				setState(136);
				expr(0);
				}
				break;
			case SMCOLON:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComandosContext extends ParserRuleContext {
		public ComandoContext comando() {
			return getRuleContext(ComandoContext.class,0);
		}
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public ComandosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comandos; }
	}

	public final ComandosContext comandos() throws RecognitionException {
		ComandosContext _localctx = new ComandosContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comandos);
		try {
			setState(144);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				comando();
				setState(141);
				comandos();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComandoContext extends ParserRuleContext {
		public SiContext si() {
			return getRuleContext(SiContext.class,0);
		}
		public ParaContext para() {
			return getRuleContext(ParaContext.class,0);
		}
		public MientrasContext mientras() {
			return getRuleContext(MientrasContext.class,0);
		}
		public Hacer_mientrasContext hacer_mientras() {
			return getRuleContext(Hacer_mientrasContext.class,0);
		}
		public SeleccionarContext seleccionar() {
			return getRuleContext(SeleccionarContext.class,0);
		}
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public Asignacion_idContext asignacion_id() {
			return getRuleContext(Asignacion_idContext.class,0);
		}
		public LeerContext leer() {
			return getRuleContext(LeerContext.class,0);
		}
		public ImprimirContext imprimir() {
			return getRuleContext(ImprimirContext.class,0);
		}
		public Llamar_funcionContext llamar_funcion() {
			return getRuleContext(Llamar_funcionContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_comando);
		try {
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				si();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				para();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(148);
				mientras();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(149);
				hacer_mientras();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(150);
				seleccionar();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(151);
				declaracion();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(152);
				asignacion_id();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(153);
				leer();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(154);
				imprimir();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(155);
				llamar_funcion();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SiContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public Expresion_logicaContext expresion_logica() {
			return getRuleContext(Expresion_logicaContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public Si_noContext si_no() {
			return getRuleContext(Si_noContext.class,0);
		}
		public SiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_si; }
	}

	public final SiContext si() throws RecognitionException {
		SiContext _localctx = new SiContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_si);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(T__9);
			setState(159);
			match(PIZQ);
			setState(160);
			expresion_logica(0);
			setState(161);
			match(PDER);
			setState(162);
			match(T__10);
			setState(163);
			comandos();
			setState(164);
			si_no();
			setState(165);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Si_noContext extends ParserRuleContext {
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public Si_noContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_si_no; }
	}

	public final Si_noContext si_no() throws RecognitionException {
		Si_noContext _localctx = new Si_noContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_si_no);
		try {
			setState(170);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(T__12);
				setState(168);
				comandos();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParaContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public List<TerminalNode> SMCOLON() { return getTokens(PsicoderParser.SMCOLON); }
		public TerminalNode SMCOLON(int i) {
			return getToken(PsicoderParser.SMCOLON, i);
		}
		public Expresion_ropContext expresion_rop() {
			return getRuleContext(Expresion_ropContext.class,0);
		}
		public Asignacion_idContext asignacion_id() {
			return getRuleContext(Asignacion_idContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public Asignacion_enteroContext asignacion_entero() {
			return getRuleContext(Asignacion_enteroContext.class,0);
		}
		public ParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para; }
	}

	public final ParaContext para() throws RecognitionException {
		ParaContext _localctx = new ParaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_para);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(T__13);
			setState(173);
			match(PIZQ);
			setState(176);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
			case SMCOLON:
				{
				setState(174);
				asignacion();
				}
				break;
			case T__15:
				{
				setState(175);
				asignacion_entero();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(178);
			match(SMCOLON);
			setState(179);
			expresion_rop();
			setState(180);
			match(SMCOLON);
			setState(181);
			asignacion_id();
			setState(182);
			match(PDER);
			setState(183);
			match(T__3);
			setState(184);
			comandos();
			setState(185);
			match(T__14);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Asignacion_enteroContext extends ParserRuleContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public Asignacion_enteroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion_entero; }
	}

	public final Asignacion_enteroContext asignacion_entero() throws RecognitionException {
		Asignacion_enteroContext _localctx = new Asignacion_enteroContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_asignacion_entero);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(T__15);
			setState(188);
			asignacion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Hacer_mientrasContext extends ParserRuleContext {
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public Expresion_ropContext expresion_rop() {
			return getRuleContext(Expresion_ropContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public Hacer_mientrasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hacer_mientras; }
	}

	public final Hacer_mientrasContext hacer_mientras() throws RecognitionException {
		Hacer_mientrasContext _localctx = new Hacer_mientrasContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_hacer_mientras);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(T__3);
			setState(191);
			comandos();
			setState(192);
			match(T__16);
			setState(193);
			match(PIZQ);
			setState(194);
			expresion_rop();
			setState(195);
			match(PDER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MientrasContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public Expresion_ropContext expresion_rop() {
			return getRuleContext(Expresion_ropContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public MientrasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mientras; }
	}

	public final MientrasContext mientras() throws RecognitionException {
		MientrasContext _localctx = new MientrasContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_mientras);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(T__16);
			setState(198);
			match(PIZQ);
			setState(199);
			expresion_rop();
			setState(200);
			match(PDER);
			setState(201);
			match(T__3);
			setState(202);
			comandos();
			setState(203);
			match(T__17);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SeleccionarContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public TerminalNode ID() { return getToken(PsicoderParser.ID, 0); }
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public CasosContext casos() {
			return getRuleContext(CasosContext.class,0);
		}
		public SeleccionarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seleccionar; }
	}

	public final SeleccionarContext seleccionar() throws RecognitionException {
		SeleccionarContext _localctx = new SeleccionarContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_seleccionar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(T__18);
			setState(206);
			match(PIZQ);
			setState(207);
			match(ID);
			setState(208);
			match(PDER);
			setState(209);
			match(T__19);
			setState(210);
			casos();
			setState(211);
			match(T__20);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CasosContext extends ParserRuleContext {
		public CasoContext caso() {
			return getRuleContext(CasoContext.class,0);
		}
		public CasosContext casos() {
			return getRuleContext(CasosContext.class,0);
		}
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public CasosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_casos; }
	}

	public final CasosContext casos() throws RecognitionException {
		CasosContext _localctx = new CasosContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_casos);
		try {
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				caso();
				setState(214);
				casos();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 2);
				{
				setState(216);
				match(T__21);
				setState(217);
				match(T__22);
				setState(218);
				comandos();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CasoContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public RomperContext romper() {
			return getRuleContext(RomperContext.class,0);
		}
		public CasoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caso; }
	}

	public final CasoContext caso() throws RecognitionException {
		CasoContext _localctx = new CasoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_caso);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(T__23);
			setState(222);
			expr(0);
			setState(223);
			match(T__22);
			setState(224);
			comandos();
			setState(225);
			romper();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Asignacion_idContext extends ParserRuleContext {
		public Id_pos_estructContext id_pos_estruct() {
			return getRuleContext(Id_pos_estructContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Asignacion_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion_id; }
	}

	public final Asignacion_idContext asignacion_id() throws RecognitionException {
		Asignacion_idContext _localctx = new Asignacion_idContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_asignacion_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			id_pos_estruct();
			setState(228);
			match(T__8);
			setState(229);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LeerContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public Id_pos_estructContext id_pos_estruct() {
			return getRuleContext(Id_pos_estructContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public TerminalNode SMCOLON() { return getToken(PsicoderParser.SMCOLON, 0); }
		public LeerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leer; }
	}

	public final LeerContext leer() throws RecognitionException {
		LeerContext _localctx = new LeerContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_leer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(T__24);
			setState(232);
			match(PIZQ);
			setState(233);
			id_pos_estruct();
			setState(234);
			match(PDER);
			setState(235);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImprimirContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public TerminalNode SMCOLON() { return getToken(PsicoderParser.SMCOLON, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Llamar_funcionContext llamar_funcion() {
			return getRuleContext(Llamar_funcionContext.class,0);
		}
		public List<TerminalNode> COMA() { return getTokens(PsicoderParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(PsicoderParser.COMA, i);
		}
		public ImprimirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprimir; }
	}

	public final ImprimirContext imprimir() throws RecognitionException {
		ImprimirContext _localctx = new ImprimirContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_imprimir);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(T__25);
			setState(238);
			match(PIZQ);
			setState(241);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(239);
				expr(0);
				}
				break;
			case 2:
				{
				setState(240);
				llamar_funcion();
				}
				break;
			}
			setState(247);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(243);
				match(COMA);
				setState(244);
				expr(0);
				}
				}
				setState(249);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(250);
			match(PDER);
			setState(251);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RomperContext extends ParserRuleContext {
		public TerminalNode SMCOLON() { return getToken(PsicoderParser.SMCOLON, 0); }
		public RomperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_romper; }
	}

	public final RomperContext romper() throws RecognitionException {
		RomperContext _localctx = new RomperContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_romper);
		try {
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				match(T__26);
				setState(254);
				match(SMCOLON);
				}
				break;
			case T__21:
			case T__23:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Llamar_funcionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsicoderParser.ID, 0); }
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public Pasar_parametrosContext pasar_parametros() {
			return getRuleContext(Pasar_parametrosContext.class,0);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public TerminalNode SMCOLON() { return getToken(PsicoderParser.SMCOLON, 0); }
		public Llamar_funcionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamar_funcion; }
	}

	public final Llamar_funcionContext llamar_funcion() throws RecognitionException {
		Llamar_funcionContext _localctx = new Llamar_funcionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_llamar_funcion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(ID);
			setState(259);
			match(PIZQ);
			setState(260);
			pasar_parametros();
			setState(261);
			match(PDER);
			setState(262);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pasar_parametrosContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(PsicoderParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(PsicoderParser.COMA, i);
		}
		public Pasar_parametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pasar_parametros; }
	}

	public final Pasar_parametrosContext pasar_parametros() throws RecognitionException {
		Pasar_parametrosContext _localctx = new Pasar_parametrosContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_pasar_parametros);
		int _la;
		try {
			setState(273);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PIZQ:
			case DOUBLE:
			case INT:
			case STRING:
			case BOOLEANO:
			case CONST:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(264);
				expr(0);
				setState(269);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMA) {
					{
					{
					setState(265);
					match(COMA);
					setState(266);
					expr(0);
					}
					}
					setState(271);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case PDER:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expresion_logicaContext extends ParserRuleContext {
		public Expresion_ropContext expresion_rop() {
			return getRuleContext(Expresion_ropContext.class,0);
		}
		public Expresion_roiContext expresion_roi() {
			return getRuleContext(Expresion_roiContext.class,0);
		}
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public List<Expresion_logicaContext> expresion_logica() {
			return getRuleContexts(Expresion_logicaContext.class);
		}
		public Expresion_logicaContext expresion_logica(int i) {
			return getRuleContext(Expresion_logicaContext.class,i);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public TerminalNode NEG() { return getToken(PsicoderParser.NEG, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ROL() { return getToken(PsicoderParser.ROL, 0); }
		public Expresion_logicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_logica; }
	}

	public final Expresion_logicaContext expresion_logica() throws RecognitionException {
		return expresion_logica(0);
	}

	private Expresion_logicaContext expresion_logica(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expresion_logicaContext _localctx = new Expresion_logicaContext(_ctx, _parentState);
		Expresion_logicaContext _prevctx = _localctx;
		int _startState = 50;
		enterRecursionRule(_localctx, 50, RULE_expresion_logica, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(285);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(276);
				expresion_rop();
				}
				break;
			case 2:
				{
				setState(277);
				expresion_roi();
				}
				break;
			case 3:
				{
				setState(278);
				match(PIZQ);
				setState(279);
				expresion_logica(0);
				setState(280);
				match(PDER);
				}
				break;
			case 4:
				{
				setState(282);
				match(NEG);
				setState(283);
				expresion_logica(2);
				}
				break;
			case 5:
				{
				setState(284);
				expr(0);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(292);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expresion_logicaContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expresion_logica);
					setState(287);
					if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
					setState(288);
					match(ROL);
					setState(289);
					expresion_logica(7);
					}
					} 
				}
				setState(294);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expresion_ropContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ROP() { return getToken(PsicoderParser.ROP, 0); }
		public Expresion_ropContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_rop; }
	}

	public final Expresion_ropContext expresion_rop() throws RecognitionException {
		Expresion_ropContext _localctx = new Expresion_ropContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_expresion_rop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			expr(0);
			setState(296);
			match(ROP);
			setState(297);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expresion_roiContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ROI() { return getToken(PsicoderParser.ROI, 0); }
		public Expresion_roiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_roi; }
	}

	public final Expresion_roiContext expresion_roi() throws RecognitionException {
		Expresion_roiContext _localctx = new Expresion_roiContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expresion_roi);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			expr(0);
			setState(300);
			match(ROI);
			setState(301);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode PIZQ() { return getToken(PsicoderParser.PIZQ, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PDER() { return getToken(PsicoderParser.PDER, 0); }
		public Llamar_funcionContext llamar_funcion() {
			return getRuleContext(Llamar_funcionContext.class,0);
		}
		public Id_pos_estructContext id_pos_estruct() {
			return getRuleContext(Id_pos_estructContext.class,0);
		}
		public TerminalNode DOUBLE() { return getToken(PsicoderParser.DOUBLE, 0); }
		public TerminalNode INT() { return getToken(PsicoderParser.INT, 0); }
		public TerminalNode CONST() { return getToken(PsicoderParser.CONST, 0); }
		public TerminalNode STRING() { return getToken(PsicoderParser.STRING, 0); }
		public TerminalNode ID() { return getToken(PsicoderParser.ID, 0); }
		public TerminalNode BOOLEANO() { return getToken(PsicoderParser.BOOLEANO, 0); }
		public TerminalNode MULOP() { return getToken(PsicoderParser.MULOP, 0); }
		public TerminalNode SUMOP() { return getToken(PsicoderParser.SUMOP, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 56;
		enterRecursionRule(_localctx, 56, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(304);
				match(PIZQ);
				setState(305);
				expr(0);
				setState(306);
				match(PDER);
				}
				break;
			case 2:
				{
				setState(308);
				llamar_funcion();
				}
				break;
			case 3:
				{
				setState(309);
				id_pos_estruct();
				}
				break;
			case 4:
				{
				setState(310);
				match(DOUBLE);
				}
				break;
			case 5:
				{
				setState(311);
				match(INT);
				}
				break;
			case 6:
				{
				setState(312);
				match(CONST);
				}
				break;
			case 7:
				{
				setState(313);
				match(STRING);
				}
				break;
			case 8:
				{
				setState(314);
				match(ID);
				}
				break;
			case 9:
				{
				setState(315);
				match(BOOLEANO);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(326);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(324);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(318);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(319);
						match(MULOP);
						setState(320);
						expr(12);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(321);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(322);
						match(SUMOP);
						setState(323);
						expr(11);
						}
						break;
					}
					} 
				}
				setState(328);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class TipoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsicoderParser.ID, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__15) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << ID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Id_pos_estructContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(PsicoderParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PsicoderParser.ID, i);
		}
		public Id_pos_estructContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_pos_estruct; }
	}

	public final Id_pos_estructContext id_pos_estruct() throws RecognitionException {
		Id_pos_estructContext _localctx = new Id_pos_estructContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_id_pos_estruct);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(331);
			match(ID);
			setState(336);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(332);
					match(T__31);
					setState(333);
					match(ID);
					}
					} 
				}
				setState(338);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 25:
			return expresion_logica_sempred((Expresion_logicaContext)_localctx, predIndex);
		case 28:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_logica_sempred(Expresion_logicaContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0156\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \3\2"+
		"\3\2\7\2C\n\2\f\2\16\2F\13\2\3\2\3\2\3\2\7\2K\n\2\f\2\16\2N\13\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6k\n\6\f\6\16\6n\13\6\3\6\5\6q\n\6"+
		"\3\7\3\7\3\7\7\7v\n\7\f\7\16\7y\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7"+
		"\b\u0083\n\b\f\b\16\b\u0086\13\b\3\b\3\b\3\t\3\t\3\t\5\t\u008d\n\t\3\n"+
		"\3\n\3\n\3\n\5\n\u0093\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\5\13\u009f\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r"+
		"\5\r\u00ad\n\r\3\16\3\16\3\16\3\16\5\16\u00b3\n\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00de\n\23\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\27\3\27\3\27\3\27\5\27\u00f4\n\27\3\27\3\27\7\27\u00f8\n\27\f\27\16"+
		"\27\u00fb\13\27\3\27\3\27\3\27\3\30\3\30\3\30\5\30\u0103\n\30\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\32\3\32\3\32\7\32\u010e\n\32\f\32\16\32\u0111\13"+
		"\32\3\32\5\32\u0114\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\5\33\u0120\n\33\3\33\3\33\3\33\7\33\u0125\n\33\f\33\16\33\u0128"+
		"\13\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u013f\n\36\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\7\36\u0147\n\36\f\36\16\36\u014a\13\36\3\37\3\37\3 \3"+
		" \3 \7 \u0151\n \f \16 \u0154\13 \3 \2\4\64:!\2\4\6\b\n\f\16\20\22\24"+
		"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>\2\3\5\2\22\22\36!\65\65\2\u0161"+
		"\2D\3\2\2\2\4Q\3\2\2\2\6U\3\2\2\2\b`\3\2\2\2\np\3\2\2\2\fr\3\2\2\2\16"+
		"|\3\2\2\2\20\u008c\3\2\2\2\22\u0092\3\2\2\2\24\u009e\3\2\2\2\26\u00a0"+
		"\3\2\2\2\30\u00ac\3\2\2\2\32\u00ae\3\2\2\2\34\u00bd\3\2\2\2\36\u00c0\3"+
		"\2\2\2 \u00c7\3\2\2\2\"\u00cf\3\2\2\2$\u00dd\3\2\2\2&\u00df\3\2\2\2(\u00e5"+
		"\3\2\2\2*\u00e9\3\2\2\2,\u00ef\3\2\2\2.\u0102\3\2\2\2\60\u0104\3\2\2\2"+
		"\62\u0113\3\2\2\2\64\u011f\3\2\2\2\66\u0129\3\2\2\28\u012d\3\2\2\2:\u013e"+
		"\3\2\2\2<\u014b\3\2\2\2>\u014d\3\2\2\2@C\5\6\4\2AC\5\f\7\2B@\3\2\2\2B"+
		"A\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GL\5\4\3\2"+
		"HK\5\6\4\2IK\5\f\7\2JH\3\2\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2"+
		"MO\3\2\2\2NL\3\2\2\2OP\7\2\2\3P\3\3\2\2\2QR\7\3\2\2RS\5\22\n\2ST\7\4\2"+
		"\2T\5\3\2\2\2UV\7\5\2\2VW\5<\37\2WX\7\65\2\2XY\7&\2\2YZ\5\n\6\2Z[\7\'"+
		"\2\2[\\\7\6\2\2\\]\5\22\n\2]^\5\b\5\2^_\7\7\2\2_\7\3\2\2\2`a\7\b\2\2a"+
		"b\5:\36\2bc\7,\2\2c\t\3\2\2\2de\5<\37\2el\7\65\2\2fg\7-\2\2gh\5<\37\2"+
		"hi\7\65\2\2ik\3\2\2\2jf\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mq\3\2\2"+
		"\2nl\3\2\2\2oq\3\2\2\2pd\3\2\2\2po\3\2\2\2q\13\3\2\2\2rs\7\t\2\2sw\7\65"+
		"\2\2tv\5\16\b\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3\2\2\2yw\3"+
		"\2\2\2z{\7\n\2\2{\r\3\2\2\2|}\5<\37\2}~\7\65\2\2~\u0084\5\20\t\2\177\u0080"+
		"\7-\2\2\u0080\u0081\7\65\2\2\u0081\u0083\5\20\t\2\u0082\177\3\2\2\2\u0083"+
		"\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\3\2"+
		"\2\2\u0086\u0084\3\2\2\2\u0087\u0088\7,\2\2\u0088\17\3\2\2\2\u0089\u008a"+
		"\7\13\2\2\u008a\u008d\5:\36\2\u008b\u008d\3\2\2\2\u008c\u0089\3\2\2\2"+
		"\u008c\u008b\3\2\2\2\u008d\21\3\2\2\2\u008e\u008f\5\24\13\2\u008f\u0090"+
		"\5\22\n\2\u0090\u0093\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u008e\3\2\2\2"+
		"\u0092\u0091\3\2\2\2\u0093\23\3\2\2\2\u0094\u009f\5\26\f\2\u0095\u009f"+
		"\5\32\16\2\u0096\u009f\5 \21\2\u0097\u009f\5\36\20\2\u0098\u009f\5\"\22"+
		"\2\u0099\u009f\5\16\b\2\u009a\u009f\5(\25\2\u009b\u009f\5*\26\2\u009c"+
		"\u009f\5,\27\2\u009d\u009f\5\60\31\2\u009e\u0094\3\2\2\2\u009e\u0095\3"+
		"\2\2\2\u009e\u0096\3\2\2\2\u009e\u0097\3\2\2\2\u009e\u0098\3\2\2\2\u009e"+
		"\u0099\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2"+
		"\2\2\u009e\u009d\3\2\2\2\u009f\25\3\2\2\2\u00a0\u00a1\7\f\2\2\u00a1\u00a2"+
		"\7&\2\2\u00a2\u00a3\5\64\33\2\u00a3\u00a4\7\'\2\2\u00a4\u00a5\7\r\2\2"+
		"\u00a5\u00a6\5\22\n\2\u00a6\u00a7\5\30\r\2\u00a7\u00a8\7\16\2\2\u00a8"+
		"\27\3\2\2\2\u00a9\u00aa\7\17\2\2\u00aa\u00ad\5\22\n\2\u00ab\u00ad\3\2"+
		"\2\2\u00ac\u00a9\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\31\3\2\2\2\u00ae\u00af"+
		"\7\20\2\2\u00af\u00b2\7&\2\2\u00b0\u00b3\5\20\t\2\u00b1\u00b3\5\34\17"+
		"\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5"+
		"\7,\2\2\u00b5\u00b6\5\66\34\2\u00b6\u00b7\7,\2\2\u00b7\u00b8\5(\25\2\u00b8"+
		"\u00b9\7\'\2\2\u00b9\u00ba\7\6\2\2\u00ba\u00bb\5\22\n\2\u00bb\u00bc\7"+
		"\21\2\2\u00bc\33\3\2\2\2\u00bd\u00be\7\22\2\2\u00be\u00bf\5\20\t\2\u00bf"+
		"\35\3\2\2\2\u00c0\u00c1\7\6\2\2\u00c1\u00c2\5\22\n\2\u00c2\u00c3\7\23"+
		"\2\2\u00c3\u00c4\7&\2\2\u00c4\u00c5\5\66\34\2\u00c5\u00c6\7\'\2\2\u00c6"+
		"\37\3\2\2\2\u00c7\u00c8\7\23\2\2\u00c8\u00c9\7&\2\2\u00c9\u00ca\5\66\34"+
		"\2\u00ca\u00cb\7\'\2\2\u00cb\u00cc\7\6\2\2\u00cc\u00cd\5\22\n\2\u00cd"+
		"\u00ce\7\24\2\2\u00ce!\3\2\2\2\u00cf\u00d0\7\25\2\2\u00d0\u00d1\7&\2\2"+
		"\u00d1\u00d2\7\65\2\2\u00d2\u00d3\7\'\2\2\u00d3\u00d4\7\26\2\2\u00d4\u00d5"+
		"\5$\23\2\u00d5\u00d6\7\27\2\2\u00d6#\3\2\2\2\u00d7\u00d8\5&\24\2\u00d8"+
		"\u00d9\5$\23\2\u00d9\u00de\3\2\2\2\u00da\u00db\7\30\2\2\u00db\u00dc\7"+
		"\31\2\2\u00dc\u00de\5\22\n\2\u00dd\u00d7\3\2\2\2\u00dd\u00da\3\2\2\2\u00de"+
		"%\3\2\2\2\u00df\u00e0\7\32\2\2\u00e0\u00e1\5:\36\2\u00e1\u00e2\7\31\2"+
		"\2\u00e2\u00e3\5\22\n\2\u00e3\u00e4\5.\30\2\u00e4\'\3\2\2\2\u00e5\u00e6"+
		"\5> \2\u00e6\u00e7\7\13\2\2\u00e7\u00e8\5:\36\2\u00e8)\3\2\2\2\u00e9\u00ea"+
		"\7\33\2\2\u00ea\u00eb\7&\2\2\u00eb\u00ec\5> \2\u00ec\u00ed\7\'\2\2\u00ed"+
		"\u00ee\7,\2\2\u00ee+\3\2\2\2\u00ef\u00f0\7\34\2\2\u00f0\u00f3\7&\2\2\u00f1"+
		"\u00f4\5:\36\2\u00f2\u00f4\5\60\31\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3"+
		"\2\2\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6\7-\2\2\u00f6\u00f8\5:\36\2\u00f7"+
		"\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2"+
		"\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7\'\2\2\u00fd"+
		"\u00fe\7,\2\2\u00fe-\3\2\2\2\u00ff\u0100\7\35\2\2\u0100\u0103\7,\2\2\u0101"+
		"\u0103\3\2\2\2\u0102\u00ff\3\2\2\2\u0102\u0101\3\2\2\2\u0103/\3\2\2\2"+
		"\u0104\u0105\7\65\2\2\u0105\u0106\7&\2\2\u0106\u0107\5\62\32\2\u0107\u0108"+
		"\7\'\2\2\u0108\u0109\7,\2\2\u0109\61\3\2\2\2\u010a\u010f\5:\36\2\u010b"+
		"\u010c\7-\2\2\u010c\u010e\5:\36\2\u010d\u010b\3\2\2\2\u010e\u0111\3\2"+
		"\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0114\3\2\2\2\u0111"+
		"\u010f\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u010a\3\2\2\2\u0113\u0112\3\2"+
		"\2\2\u0114\63\3\2\2\2\u0115\u0116\b\33\1\2\u0116\u0120\5\66\34\2\u0117"+
		"\u0120\58\35\2\u0118\u0119\7&\2\2\u0119\u011a\5\64\33\2\u011a\u011b\7"+
		"\'\2\2\u011b\u0120\3\2\2\2\u011c\u011d\7(\2\2\u011d\u0120\5\64\33\4\u011e"+
		"\u0120\5:\36\2\u011f\u0115\3\2\2\2\u011f\u0117\3\2\2\2\u011f\u0118\3\2"+
		"\2\2\u011f\u011c\3\2\2\2\u011f\u011e\3\2\2\2\u0120\u0126\3\2\2\2\u0121"+
		"\u0122\f\b\2\2\u0122\u0123\7+\2\2\u0123\u0125\5\64\33\t\u0124\u0121\3"+
		"\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127"+
		"\65\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\5:\36\2\u012a\u012b\7*\2\2"+
		"\u012b\u012c\5:\36\2\u012c\67\3\2\2\2\u012d\u012e\5:\36\2\u012e\u012f"+
		"\7)\2\2\u012f\u0130\5:\36\2\u01309\3\2\2\2\u0131\u0132\b\36\1\2\u0132"+
		"\u0133\7&\2\2\u0133\u0134\5:\36\2\u0134\u0135\7\'\2\2\u0135\u013f\3\2"+
		"\2\2\u0136\u013f\5\60\31\2\u0137\u013f\5> \2\u0138\u013f\7\60\2\2\u0139"+
		"\u013f\7\61\2\2\u013a\u013f\7\64\2\2\u013b\u013f\7\62\2\2\u013c\u013f"+
		"\7\65\2\2\u013d\u013f\7\63\2\2\u013e\u0131\3\2\2\2\u013e\u0136\3\2\2\2"+
		"\u013e\u0137\3\2\2\2\u013e\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e\u013a"+
		"\3\2\2\2\u013e\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013f"+
		"\u0148\3\2\2\2\u0140\u0141\f\r\2\2\u0141\u0142\7.\2\2\u0142\u0147\5:\36"+
		"\16\u0143\u0144\f\f\2\2\u0144\u0145\7/\2\2\u0145\u0147\5:\36\r\u0146\u0140"+
		"\3\2\2\2\u0146\u0143\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148"+
		"\u0149\3\2\2\2\u0149;\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\t\2\2\2"+
		"\u014c=\3\2\2\2\u014d\u0152\7\65\2\2\u014e\u014f\7\"\2\2\u014f\u0151\7"+
		"\65\2\2\u0150\u014e\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152"+
		"\u0153\3\2\2\2\u0153?\3\2\2\2\u0154\u0152\3\2\2\2\33BDJLlpw\u0084\u008c"+
		"\u0092\u009e\u00ac\u00b2\u00dd\u00f3\u00f9\u0102\u010f\u0113\u011f\u0126"+
		"\u013e\u0146\u0148\u0152";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}