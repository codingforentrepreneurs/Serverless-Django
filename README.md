[![Serverless Django Logo](https://static.codingforentrepreneurs.com/media/projects/serverless-django/images/share/Serverless_Django_with_GCloud_-_Share.jpg)](https://www.codingforentrepreneurs.com/projects/serverless-django)

# Serverless Django
[Learn](https://www.codingforentrepreneurs.com/projects/serverless-django) to build and deploy a Serverless Django application to Google Cloud Run with Cloud SQL, Cloud Build, &amp; Docker.

### Requirements
- Python XP -> found [here](https://cfe.sh/projects/30-days-python-38) 

- Django XP -> found [here](https://cfe.sh/t/try-django)

- Google SDK & CLI Installed via [This guide Guide](https://kirr.co/03zjn0)

### Recommended
- [Serverless Python Web App Tutorial](https://kirr.co/blqkyw)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)


### Reference 
- [Serverless Django Guide](https://kirr.co/9nirqh)
- [Staging Django Guide](https://kirr.co/f0ndg6)
- [Serverless Django Tutorial](https://kirr.co/zqwkw6)


### To use this code

**1. Clone**
```
git clone https://github.com/codingforentrepreneurs/Serverless-Django .
```

**2. Create Virtual Environment**
```bash
cd supercharged
python3.8 -m venv .
```
> Use Any version of Python >= 3.6

**3. Activate virtual environment**
Mac/Linux
```
source bin/activate
```

Windows:
```
.\Scripts\activate
```

> If using **pipenv**, run `pipenv shell` && `pipenv install`


**4. Install requirements**

```
pip install -r requirements.txt
```

**5. Run locally**
Mac/Linux
```
chmod +x ./scripts/local.sh
./scripts/local.sh
```

Windows
```powershell
.\scripts\local.ps1
```


### Lesson Code Reference
[3 - Virtual Environment with Pipenv & VSCode Workspace](../../tree/e763f8433cfbec95b36c913b895c8abf5d126379/)

[4 - Staging Django for Production](../../tree/6e725d7c1925f6b5c5acbfe62fa2365f0ce88265/)

[5 - Home Page View including Settings Variables](../../tree/69bd382712a1b4e9549df8ec4d03f562ef60273b/)

[6 - WSGI with Gurnicorn or Waitress](../../tree/bef3f532be62f0b7dae0c274071a003a253cc8c8/)

[8 - Install the Cloud SQL Proxy](../../tree/3a9ebdd3f58ea26a48c8f3d61e8762b092e08e8f/)

[9 - Database Service Account directory holder](../../tree/e9e1d81671b9ca4593ca6e67cfafa6a614a67960/)

[10 - Run Cloud SQL Proxy with Service Account](../../tree/b2d8ab451f9947d7eb9083d746650b87df4abf01/)

[11 - Connect Django & Proxy Database](../../tree/0fcb9120f40577e8156d12ff967af7c93a609450/)

[12 - Dockerfile, Docker Build, & Docker Run](../../tree/ef83da89db128e38ef236ed5ebdbba4f2fec7c26/)

[13 - Docker Build & Push To GCloud Container Registry](../../tree/b3809c468dedca85461b88e75584627eb948987c/)

[14 - Google Cloud Build](../../tree/a62632df2c2b1dc42618f48db67317796bc0a079/)

[15 - Deploy to Cloud Run](../../tree/b63014aaef33d234df4391a7c1d47ca4dfb4bd9e/)

[16 - Make Changes, Build, & Deploy](../../tree/f8dc89c362621285806e29270013ccdecae16694/)

[17 - Production Database on Cloud Run](../../tree/c07898ae0df4431aa8449a9c05655bb8020fcd90/)

[18 - Thank you and next steps](../../tree/a31522692924576b82fda5c023a49cd750e23209/)

