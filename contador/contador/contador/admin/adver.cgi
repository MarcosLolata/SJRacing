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
############# Nada abaixo desta linha precisa ser Editado ################
&mostra;

sub mostra {
print "Content-type: text/html\n\n";
open (MOSTRA,"$diretorio/conta.txt");
$numero = <MOSTRA>;
close <MOSTRA>;
open (IP2, "$diretorio/ipcheca.txt");
$mostraip = <IP2>;
close <IP2>;
open (REL, "$diretorio/relogio.txt");
$relogio = <REL>;
close <REL>;
print "<p><b>Contador:</b> <font color=\"$cor_fonte\" face=\"$tipo\" size=\"$tamanho\">$numero</font></p>\n";
print "<p><b>Ultimo IP:</b> $mostraip</p> \n";
print "<p><b>Ultima Visita:</b> $relogio</p> \n";
}
