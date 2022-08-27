# Referrer Spam Blocker

Most referral blockers for NGINX absolutely suck by using a `map` with thousands of regular expressions.
This comes with a huge performance penalty due to regular expressions being evaluated sequentially.

This blocker uses the proper spam bocking technique (tm), which won't ruin your performance!

## Installation

Drop the file to an included directory, e.g. `/etc/nginx/conf.d`:

```bash
curl -o /etc/nginx/conf.d/referral-spam.conf https://raw.githubusercontent.com/dvershinin/referrer-spam-blocker/main/referral-spam.conf
```

Add the following to each `/etc/nginx/site-available/example.com.conf` that needs protection:

```nginx
      server {
        if ($bad_referer) {
          return 444;
        }
      }
```

Check NGINX configuration for error by running `nginx -t`. If all good, reload NGINX:

```bash
systemctl reload nginx
```

That's it. No more annoying spammers.