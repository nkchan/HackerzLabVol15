use strict;
use LWP::UserAgent;
use HTTP::Request::Common;

# POST準備
my $url = 'https://9bqcyrr7bb.execute-api.ap-northeast-1.amazonaws.com/dev/Q14';
my %postdata = ( 'id' => 'id', 'pass' => 'pass' );
my $request = POST( $url, \%postdata );

# 送信
my $ua = LWP::UserAgent -> new;
my $res = $ua -> request( $request ) -> as_string;
