#!/usr/local/bin/perl
########################################################
# Contador                                  versão 1.0 #
########################################################
# Por Guilherme Marques             guizero@bol.com.br #
# 02 de Agosto de 2000                                 #
########################################################
# Qualquer duvida, envie-me um email                   #
########################################################
require "admin/dados.pl";
############# Nada abaixo desta linha precisa ser Editado ################
$ipvisitante = $ENV{'REMOTE_ADDR'};
&abre_e_conta; 
&mostra;
&feliz;

sub abre_e_conta {
open (DATA,"$diretorio/conta.txt");
@numero = <DATA>;
close (DATA);
$conta = $numero[0];
&checaip;
open (DATA2,">$diretorio/conta.txt");
print DATA2 $conta;
close(DATA2);
}

sub mostra {
open (MOSTRA,"$diretorio/conta.txt");
$numero = <MOSTRA>;
close (MOSTRA);
open (IP2, ">$diretorio/ipcheca.txt");
print IP2 $ipvisitante;
close (IP2);
if ($invisivel eq "s") {
print "Content-type: text/html\n\n";
print "<font></font>\n";
}
else {
print "Content-type: text/html\n\n";
print "<font color=\"$cor_fonte\" face=\"$tipo\" size=\"$tamanho\">$numero</font>\n";
}
}

sub checaip {
open (IP,"$diretorio/ipcheca.txt");
@ip = <IP>;
close (IP);
$ultimoip = $ip[0];
if ($ultimoip eq "$ipvisitante") {
$conta;
}
else {
$conta++
}
}

sub feliz {
open (REL,"$diretorio/relogio.txt");
$formato1 = <REL>;
close (REL);
@dias = ('Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado');
@m = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro');
@meses = ('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez');
@mesnum = ('1','2','3','4','5','6','7','8','9','10','11','12');

($BRseg, $BRmin, $BRhora, $BRmdia, $BRmes, $BRano, $BRsdia, $BRadia, $BRisdst) = gmtime(time-(10800));

if ($BRhora < 10) {
$BRhora = "0$BRhora";
}
if ($BRmin < 10) {
$BRmin = "0$BRmin";
}
if ($BRseg < 10) { 
$BRsec = "0$BRsec"; 
}
if ($BRmdia < 10) { 
$BRmdia = "0$BRmdia"; 
}
$BRano = 1900 + $BRano;

$formato1 = "Dia $BRmdia de @m[$BRmes] de $BRano, $BRhora:$BRmin:$BRseg";
open (REL,">$diretorio/relogio.txt");
print REL $formato1;
close (REL);
}


