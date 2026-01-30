#!/usr/local/bin/perl
########################################################
# Contador                                  versão 1.0 #
########################################################
# Por Guilherme Marques             guizero@bol.com.br #
# 02 de Agosto de 2000                                 #
########################################################
# Qualquer duvida, envie-me um email                   #
########################################################
require "dados.pl";

&init_cgi;
if ($in{'funcao'} eq "1") {
&server;
exit;
}
elsif ($in{'funcao'} eq "2") {
&contador;
exit;
}
elsif ($in{'funcao'} eq "3") {
&como;
exit;
}
elsif ($in{'funcao'} eq "4") {
&senha;
exit;
}
elsif ($in{'funcao'} eq "5") {
&ver;
exit;
}
elsif ($in{'funcao'} eq "6") {
&adiciona_e_reseta;
exit;
}
elsif ($in{'funcao'} eq "senha") {
&criasenha;
exit;
}
elsif ($in{'funcao'} eq "adiciona") {
&adiciona;
&menu;
exit;
}
elsif ($in{'funcao'} eq "reseta") {
&reseta;
&menu;
exit;
}
else {
&clean_data;
&update_data;
&menu;
}

sub menu {
print "Content-type: text/html\n\n";

$info = "<html><head><title>Administração do Contador</title></head><body bgcolor=\"#ffffff\" link=\"#000000\" vlink=\"#000000\">";
$info .= "<p align=\"center\"><big><strong><font face=\"Verdana\" color=\"#FF0000\">Contador </font>";
$info .= "<font face=\"Verdana\" color=\"#400080\"><big><big>Admin</big></big></font></strong></big></p>";
$info .= "<div align=\"center\"><center>";
$info .= "<table border=\"2\" cellpadding=\"0\" cellspacing=\"0\" width=\"367\" bordercolor=\"#000000\" bordercolorlight=\"#000000\" bordercolordark=\"#000000\">";
$info .= "<tr>";
$info .= "<td width=\"365\" bgcolor=\"#000080\"><p align=\"center\"><font face=\"Verdana\" color=\"#FFFFFF\"><strong>Escolha o que deseja fazer</strong></font></td>";
$info .= "</tr><tr>";
$info .= "<td width=\"365\"><p align=\"center\"><a href=\"admin.cgi?funcao=1\">Configurar Servidor</a></td>";
$info .= "</tr>";
$info .= "<tr>";
$info .= "<td width=\"365\"><p align=\"center\"><a href=\"admin.cgi?funcao=2\">Configurar Contador</a></td>";
$info .= "</tr>";
$info .= "<tr>";
$info .= "<td width=\"365\"><p align=\"center\"><a href=\"admin.cgi?funcao=3\">Como colocar o Contador na Pagina?</a></td>";
$info .= "</tr>";
$info .= "<tr>";
$info .= "<td width=\"365\"><p align=\"center\"><a href=\"admin.cgi?funcao=4\">Criar arquivo de proteção do Admin</a></td>";
$info .= "</tr>";
$info .= "<tr>";
$info .= "<td width=\"365\"><p align=\"center\"><a href=\"admin.cgi?funcao=5\">Veja como vai o seu Contador</a></td>";
$info .= "</tr>";
$info .= "<tr>";
$info .= "<td width=\"365\"><p align=\"center\"><a href=\"admin.cgi?funcao=6\">Adicione ou resete seu Contador</a></td>";
$info .= "</tr>";
$info .= "<tr>";
$info .= "<td width=\"365\" bgcolor=\"#000080\">&nbsp;</td>";
$info .= "</tr>";
$info .= "</table></center></div></body></html>";

print $info
}


sub server {
print "Content-type: text/html\n\n";
print <<EOF;
<html>

<head>
<title>Configura o Servidor</title>
</head>

<body>

<p align="center"><big><strong><font face="Verdana" color="#FF0000">Contador </font><font
face="Verdana" color="#400080"><big><big>Admin</big></big></font></strong></big></p>
<div align="center"><center>

<table border="2" cellpadding="0" cellspacing="0" width="367" bordercolor="#000000"
bordercolorlight="#000000" bordercolordark="#000000">
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><font face="Verdana" color="#FFFFFF"><strong>Configure
    de acordo com o seu Servidor</strong></font></td>
  </tr>
  <tr>
    <td width="365"><form method="POST" action="admin.cgi">
      <div align="left"><p>Escreva o Path (não a URL) do diretorio onde esta o arquivo conta.txt: (ex:/data1/hypermart.net/usuario/contador) </p>
      </div><div align="center"><center><p><input type="text" size="40" name="diretorio"
      value="$diretorio"></p>
      </center></div><div align="left"><p>Escreva a URL do diretorio onde esta o arquivo conta.txt: (ex:http://usuario.hypermart.net/contador) </p>
      </div><div align="center"><center><p><input type="text" size="40" name="url"
      value="$url"></p>
      </center></div>
<div align="center"><center><p><input type="submit" value="Configurar" name="configura"></p>
      </center></div>
    </form>
    </td>
  </tr>
  <tr>
    <td width="365" bgcolor="#000080">&nbsp;</td>
  </tr>
</table>
</center></div>
</body>
</html>
EOF
exit;
}

sub contador {
print "Content-type: text/html\n\n";
print <<EOF;
<html>

<head>
<title>Contador - Administração</title>
</head>

<body>

<p align="center"><big><strong><font face="Verdana" color="#FF0000">Contador </font><font
face="Verdana" color="#400080"><big><big>Admin</big></big></font></strong></big></p>
<div align="center"><center>

<table border="2" cellpadding="0" cellspacing="0" width="367" bordercolor="#000000"
bordercolorlight="#000000" bordercolordark="#000000">
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><font face="Verdana" color="#FFFFFF"><strong>Configure
    de acordo com a sua Pagina</strong></font></td>
  </tr>
  <tr>
    <td width="365"><form method="POST" action="admin.cgi">
      <div align="center"><p>Qual a cor do Contador? (ex: #000000)</p>
      </div><div align="center"><center><p><input type="text" size="40" name="cor_fonte"
      value="$cor_fonte"></p>
      </center></div><div align="center"><p>Qual a fonte do Contador? (ex: Arial)</p>
      </div><div align="center"><center><p><input type="text" size="40" name="tipo"
      value="$tipo"></p>
      </center></div><div align="center"><p>Qual o tamanho do Contador? (ex: 4)</p>
      </div><div align="center"><center><p><input type="text" size="40" name="tamanho"
      value="$tamanho"></p>
      </center></div><div align="center"><p>Invisivel? (se quiser, escolha "s", caso
      contrario, "n")</p>
      </div><div align="center"><p><input type="text" size="40" name="invisivel"
      value="$invisivel"></p>
      </center></div>
      </div><div align="center"><center><p><input type="submit" value="Configurar"
      name="configura"></p>
      </center></div>
    </form>
    </td>
  </tr>
  <tr>
    <td width="365" bgcolor="#000080">&nbsp;</td>
  </tr>
</table>
</center></div>
</body>
</html>
EOF
exit;
}

sub como {
print "Content-type: text/html\n\n";
print <<EOF;
<html>

<head>
<title>Contador - Administração</title>
</head>

<body>

<p align="center"><big><strong><font face="Verdana" color="#FF0000">Contador </font><font
face="Verdana" color="#400080"><big><big>Admin</big></big></font></strong></big></p>
<div align="center"><center>

<table border="2" cellpadding="0" cellspacing="0" width="367" bordercolor="#000000"
bordercolorlight="#000000" bordercolordark="#000000">
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><font face="Verdana" color="#FFFFFF"><strong>Como
    colocar em sua Pagina</strong></font></td>
  </tr>
  <tr>
    <td width="365">Para colocar o contador em sua página não é dificil, o seu servidor
    deve ter acesso a SSI, para saber se tem ou não, pergunte para os administradores de seu
    servidor. Caso não tenha, o endereço <a href="http://www.hypermart.net">www.hypermart.net</a>
    contem SSI e CGI/PERL, tudo necessario para rodar o contador!<p>Se tudo já esta pronto
    para rodar o Contador, inclua em sua pagina o seguinte codigo:</p>
    <p align="center">&lt;!--#exec cgi=&quot;/cgi-bin/contador/contador.cgi&quot;--&gt;</p>
    <p>Qualquer duvida, envie um email para:</p>
    <p><a href="mailto:guizero\@bol.com.br">guizero\@bol.com.br</a> </td>
  </tr>
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><a href="admin.cgi"><font
    color="#FFFFFF">Voltar para o Admin</font></a></td>
  </tr>
</table>
</center></div>
</body>
</html>

EOF
exit;
}

sub senha {
print "Content-type: text/html\n\n";
print <<EOF;
<html>

<head>
<title>Contador - Administração</title>

</head>

<body>

<p align="center"><big><strong><font face="Verdana" color="#FF0000">Contador </font><font
face="Verdana" color="#400080"><big><big>Admin</big></big></font></strong></big></p>
<div align="center"><center>

<table border="2" cellpadding="0" cellspacing="0" width="367" bordercolor="#000000"
bordercolorlight="#000000" bordercolordark="#000000">
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><font face="Verdana" color="#FFFFFF"><strong>Coloque
    sua senha de Inicio</strong></font></td>
  </tr>
  <tr>
    <td width="365"><form method="POST" action="admin.cgi">
      <input type="hidden" name="action" value="encrypt"><p>Primeiro Passo: Entre com o seu
      Login: <input type="text" name="username" size="20"></p>
      <p>Segundo Passo: Entre com a sua senha: <input type="text" name="password" size="20"></p>
      <p>Leia com atenção:</p>
      <p>Lembre-se que apos criar seu arquivo de proteção do Admin, o login e senha será
      pedido somente uma vez por sessão, então não se desespere. E a cada vez que você
      reconectar, será pedido denovo</p>
      <div align="center"><center><p><input type="submit" value="Pronto" name="B1">
<input type="hidden" value="senha" name="funcao"></p>
      </center></div>
    </form>
    </td>
  </tr>
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><a href="admin.cgi"><font
    color="#FFFFFF">Voltar para o Admin</font></a></td>
  </tr>
</table>
</center></div>
</body>
</html>

EOF
exit;
}

sub criasenha {
$htpasswd = $ENV{SCRIPT_FILENAME};
for ($htpasswd) {
s/admin.cgi/.htpasswd/g;
}
$password = crypt($in{'password'}, "Cd");
open (PASS, ">$htpasswd");
print PASS "$in{'username'}:$password\n";
close (PASS);

$htaccess = $ENV{SCRIPT_FILENAME};
for ($htaccess) {
s/admin.cgi/.htaccess/g;
}
$filetext = "AuthName \"Admin do Contador\"\n";
$filetext .= "AuthType Basic\n";
$filetext .= "AuthUserFile $htpasswd\n";
$filetext .= "<Limit GET>\n";
$filetext .= "require valid-user\n";
$filetext .= "</Limit>\n"; 

open (ACCESS, ">$htaccess");
print ACCESS "$filetext\n";
close (ACCESS);

print "Location: #\n\n";

}

sub ver {
print "Content-type: text/html\n\n";
print <<EOF;
<html>

<head>
<title>Contador - Administração</title>
</head>

<body>

<p align="center"><big><strong><font face="Verdana" color="#FF0000">Contador </font><font
face="Verdana" color="#400080"><big><big>Admin</big></big></font></strong></big></p>
<div align="center"><center>

<table border="2" cellpadding="0" cellspacing="0" width="367" bordercolor="#000000"
bordercolorlight="#000000" bordercolordark="#000000">
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><font face="Verdana" color="#FFFFFF"><strong>Como
    esta seu Contador</strong></font></td>
  </tr>
  <tr>
    <td width="365"><form method="POST" action="admin.cgi">
      <input type="hidden" name="action" value="encrypt"><input type="hidden" name="funcao"
      value="senha"><p>Aqui você sabe como está seu contador, bom para que escolheu a versão
      invisivel.</p>
      <p>&nbsp;</p>
      <p align="center"> <!--#exec cgi="adver.cgi"--> </p>
      <p>&nbsp;</p>
    </form>
    </td>
  </tr>
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><a href="admin.cgi"><font
    color="#FFFFFF">Voltar para o Admin</font></a></td>
  </tr>
</table>
</center></div>
</body>
</html>
EOF
exit;
}

sub init_cgi {

	my $length = $ENV{CONTENT_LENGTH};
	my $query = $ENV{QUERY_STRING};
	my (@assign);

	if ($query){
		@assign = split(/&/,$query);
		$formlength = @assign;
		}

	elsif ($length) {
		read(STDIN, $_, $length);
		chomp;
		@assign = split('&');
		$formlength = @assign;
		}

	else {
		$formlength = 0;
		}

	for (my $i=0; $i<$formlength; $i++) {
		my ($name,$value) = split('=',$assign[$i]);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fFA-F0-9][a-fFA-F0-9])/pack("C", hex($1))/eg;
		$value =~ s/~!/ ~!/g;
		
			if (defined($in{$name})) {
			$in{$name} .= ",$value";
			}

			else {
			$in{$name} = $value;
			}
		}

}

sub clean_data {
if ($in{'diretorio'} eq "") {
$in{'diretorio'} = $diretorio;
}
if ($in{'url'} eq "") {
$in{'url'} = $url;
}
if ($in{'cor_fonte'} eq "") {
$in{'cor_fonte'} = $cor_fonte;
}
if ($in{'invisivel'} eq "") {
$in{'invisivel'} = $invisivel;
}
if ($in{'tipo'} eq "") {
$in{'tipo'} = $tipo;
}
if ($in{'tamanho'} eq "") {
$in{'tamanho'} = $tamanho;
}
if ($in{'digitos'} eq "") {
$in{'digitos'} = $digitos;
}
}

sub update_data {
$newuser .= "\#CUIDADO - Não edite este arquivo\n";
$newuser .= "\$diretorio=\"$in{'diretorio'}\";\n";
$newuser .= "\$url=\"$in{'url'}\";\n";
$newuser .= "\$cor_fonte=\"$in{'cor_fonte'}\";\n";
$newuser .= "\$invisivel=\"$in{'invisivel'}\";\n";
$newuser .= "\$tipo=\"$in{'tipo'}\";\n";
$newuser .= "\$tamanho=\"$in{'tamanho'}\";\n";
$newuser .= "\$digitos=\"$in{'digitos'}\";\n";
$newuser .= "1\;";
open(NEWUSER,">dados.pl");
print NEWUSER $newuser;
close(NEWUSER);
}

sub adiciona_e_reseta {
print "Content-type: text/html\n\n";
print <<EOF;
<html>

<head>
<title>Contador - Administração</title>
</head>

<body>

<p align="center"><big><strong><font face="Verdana" color="#FF0000">Contador </font><font
face="Verdana" color="#400080"><big><big>Admin</big></big></font></strong></big></p>
<div align="center"><center>

<table border="2" cellpadding="0" cellspacing="0" width="367" bordercolor="#000000"
bordercolorlight="#000000" bordercolordark="#000000">
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><font face="Verdana" color="#FFFFFF"><strong>Adicione
    ou Resete seu Contador</strong></font></td>
  </tr>
  <tr>
    <td width="365"><form method="POST" action="admin.cgi">
      <input type="hidden" name="funcao" value="adiciona"><div align="center"><center><p>Se
      você quiser adicionar ao seu contador um certo numero, digite quanto abaixo e clique em
      &quot;Adicionar<input type="text" name="quanto" size="15"> <input type="submit"
      value="Adicionar" name="dah"> </p>
      </center></div>
    </form>
    <form>
      <input type="hidden" name="funcao" value="reseta"><div align="center"><div align="center"><center><p>Se
      você quiser resetar o contador e deixalo em 0, clique no botão abaixo.</p>
      </center></div><div align="center"><center><p><input type="submit" value="Resetar"
      name="dah"></p>
      </center></div></div><p>&nbsp;</p>
    </form>
    </td>
  </tr>
  <tr>
    <td width="365" bgcolor="#000080"><p align="center"><a href="admin.cgi"><font
    color="#FFFFFF">Voltar para o Admin</font></a></td>
  </tr>
</table>
</center></div>
</body>
</html>

EOF
exit;
}

sub adiciona {
open (ADD,"$diretorio/conta.txt");
$numero = <ADD>;
close (ADD);
$num = $numero + $in{'quanto'};
open (ADD2,">$diretorio/conta.txt");
print ADD2 $num;
close (ADD2);
}

sub reseta {
open (ADD,"$diretorio/conta.txt");
$numero = <ADD>;
close (ADD);
$num = $numero - $numero;
open (ADD2,">$diretorio/conta.txt");
print ADD2 $num;
close (ADD2);
}


