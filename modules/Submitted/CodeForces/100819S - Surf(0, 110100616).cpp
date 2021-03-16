#include <bits/stdc++.h>
using namespace std;

typedef long long           ll;
typedef long double         ld;
typedef unsigned long       ul;
typedef unsigned long long  ull;
typedef vector<ll>          vll;
typedef vector<int>         vi;
typedef pair<int,int>       pii;
typedef pair<ll,ll>         pll;
typedef pair<ld,ld>         pld;
typedef vector< pii >       vii;

#define fastIO              ios::sync_with_stdio(false);    cin.tie(nullptr);   cout.tie(nullptr)
#pragma GCC optimize("Ofast,no-stack-protector")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
#pragma G++ optimize("Ofast,no-stack-protector")
#pragma G++ target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma G++ optimize("unroll-loops")

#define MX                  INT_MAX
#define MN                  INT_MIN
#define MAX                 2000005
#define MOD                 1000000007
#define eps                 1e-9
#define INF                 0x3f3f3f3f3f3f3f3f /// 4,557,430,888,798,830,399
#define inf                 0x3f3f3f3f /// 1,061,109,567
#define PI                  acos(-1.0)  /// 3.1415926535897932

#define pb                  push_back
#define ppb                 pop_back
#define mp                  make_pair
#define ff                  first
#define ss                  second
#define sf                  scanf
#define pf                  printf
#define pn                  pf("\n")
#define sfi(x)              sf("%d", &x)
#define sfii(x, y)          sf("%d %d", &x, &y)
#define sfiii(x, y, z)      sf("%d %d %d", &x, &y, &z)
#define sfiiii(w, x, y, z)  sf("%d %d %d %d", &w, &x, &y, &z)
#define sfl(x)              sf("%lld", &x)
#define sfll(x, y)          sf("%lld %lld", &x, &y)
#define sflll(x, y, z)      sf("%lld %lld %lld", &x, &y, &z)
#define sfllll(w, x, y, z)   sf("%lld %lld %lld %lld", &w, &x, &y, &z)
#define pfi(x)              pf("%d\n", x)
#define pfii(x, y)          pf("%d %d\n", x, y)
#define pfiii(x, y, z)      pf("%d %d %d\n", x, y, z)
#define pfl(x)              pf("%lld\n", x)
#define pfll(x, y)          pf("%lld %lld\n", x, y)
#define pflll(x, y, z)      pf("%lld %lld %lld\n", x, y, z)
#define gl(a)               getline(cin,a)
#define pfs(a)              pf("%s\n", a)
#define pfc(a)              pf("%c", a)
#define yes                 pf("YES\n")
#define no                  pf("NO\n")
#define sqr(x)              ((x)*(x))
#define loop(i, y)          for(int i=0; i<int(y); i++)
#define FOR(i, x, y)        for(int i=int(x); i<=int(y); i++)
#define ROF(i, x, y)        for(int i=int(x); i>=int(y); i--)
#define all(c)              c.begin(), c.end()
#define sz(c)               int(c.size())
#define clr(x, y)           memset(x, y, sizeof(x))
#define arini(ar, x, y)     for(int i=x;i<=y;i++){ sfi(ar[i]);}
#define arinll(ar, x, y)    for(int i=x;i<=y;i++){ sfl(ar[i]);}
#define arouti(ar, x, y)	for(int i=x;i<=y;i++){ pf("%d", ar[i]); if(i<y) pf(" "); else pf("\n");}
#define aroutll(ar, x, y)	for(int i=x;i<=y;i++){ pf("%lld", ar[i]); if(i<y) pf(" "); else pf("\n");}
#define vini(v, y)          int w; for(int i=0;i<y;i++){ sfi(w); v.pb(w);}
#define vinll(v, y)         ll w; for(int i=0;i<y;i++){ sfl(w); v.pb(w);}
#define vouti(v)            int g=v.size(); for(int i=0;i<g;i++){ pf("%d", v[i]); if(i<g-1) pf(" "); else pf("\n");}
#define voutll(v)           int g=v.size(); for(int i=0;i<g;i++){ pf("%lld", v[i]); if(i<g-1) pf(" "); else pf("\n");}
#define test(tt)            for(int cas=1;cas<=tt;cas++)
#define max3(a,b,c)         max(max(a,b),c)
#define max4(a,b,c,d)       max(max3(a,b,c),d)
#define min3(a,b,c)         min(min(a,b),c)
#define min4(a,b,c,d)       min(min3(a,b,c),d)
#define even(n)             if(n%2==0)
#define odd(n)              if(n%2==1)
#define Unique(a)   		sort(all(a)), a.erase(unique(all(a)),a.end())
#define sp					<< " " <<
#define ps					pf(" ")
#define pf1(a)				cout << a << endl
#define pfm					pf1(-1)

template <class T> inline T bigMod(T p,T e,T M){ T ret = 1; for(; e > 0; e >>= 1){ if(e & 1) ret = (ret * p) % M; p = (p * p) % M; } return (T) ret;}
template <class T> inline T modInverse(T a,T M){return bigMod(a,M-2,M);}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T lcm(T a,T b) {a=abs(a);b=abs(b); return (a/gcd(a,b))*b;}
template <class T> inline bool isprime(T n){if(n<2)return false;for(ll i=2;i*i<=n;i++){if(n%i==0)return false;}return true;}
#define input               freopen("input.txt","r",stdin);
#define output              freopen("output.txt","w",stdout);
/* //////////////////////////START\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ */
#define Max 1000005
int dp[MAX], tt[Max], wt[Max], point[Max];
int main()
{
    #ifdef eXtinct
        clock_t tStart = clock();
        //input;
        //output
    #endif
	int n, i;
	sfi(n);
	int mx=MN;
	map < int, pii > m;
	for(i=1; i<=n; i++){
		int x, y, z;
		sfiii(x, y, z);
		m[x]={y, z};
		if(x>mx) mx=x;
	}
	dp[mx+1]=0;
	for(i=mx+1; i>=1; i--){
		dp[i]=dp[i+1];
		//cout << m[i].ss sp m[i].ff << endl;
		dp[i]=max(dp[i], dp[i + m[i].ss] + m[i].ff);
	}
	pfi(dp[1]);
	#ifdef eXtinct
        printf("\nRuntime:: %.10fs\n", (double)(clock()-tStart)/CLOCKS_PER_SEC);
    #endif
    return 0;
}
