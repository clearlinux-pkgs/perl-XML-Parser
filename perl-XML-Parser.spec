#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Parser
Version  : 2.44
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-2.44.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-2.44.tar.gz
Summary  : 'A perl module for parsing XML documents'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-XML-Parser-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : expat-dev
BuildRequires : perl(LWP::UserAgent)

%description
XML::Parser Version 2.40
All rights reserved.
This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-XML-Parser package.
Group: Development
Requires: perl-XML-Parser-lib = %{version}-%{release}
Provides: perl-XML-Parser-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-Parser package.


%package lib
Summary: lib components for the perl-XML-Parser package.
Group: Libraries

%description lib
lib components for the perl-XML-Parser package.


%prep
%setup -q -n XML-Parser-2.44

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/Japanese_Encodings.msg
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/README
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/big5.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/euc-kr.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/ibm866.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-2.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-3.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-4.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-5.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-7.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-8.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-9.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/koi8-r.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1250.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1251.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1252.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1255.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-euc-jp-jisx0221.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-euc-jp-unicode.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-cp932.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-jdk117.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-jisx0221.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-unicode.enc
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Expat.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/LWPExternEnt.pl
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Style/Debug.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Style/Objects.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Style/Stream.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Style/Subs.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/XML/Parser/Style/Tree.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Parser.3
/usr/share/man/man3/XML::Parser::Expat.3
/usr/share/man/man3/XML::Parser::Style::Debug.3
/usr/share/man/man3/XML::Parser::Style::Objects.3
/usr/share/man/man3/XML::Parser::Style::Stream.3
/usr/share/man/man3/XML::Parser::Style::Subs.3
/usr/share/man/man3/XML::Parser::Style::Tree.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/XML/Parser/Expat/Expat.so
