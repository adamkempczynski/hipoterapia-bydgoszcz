# Decap CMS - Technical Documentation

## Quick Start

### Local Development

1. **Start the Astro dev server:**
   ```bash
   npm run dev
   ```

2. **In a separate terminal, start the CMS backend:**
   ```bash
   npm run cms
   ```

3. **Access the admin panel:**
   ```
   http://localhost:4322/admin/
   ```

4. **No authentication required** in local mode - the CMS will work directly with your local files.

---

## Configuration Files

### `/public/admin/config.yml`
Main CMS configuration file:
- **Backend**: Git Gateway (production) / Local Backend (development)
- **Collections**: Defines content types (aktualnosci)
- **Media**: Uploads go to `public/uploads/`
- **Locale**: Set to Polish (`pl`)
- **Workflow**: Editorial workflow enabled (draft/review/publish)

### `/public/admin/index.html`
Admin panel entry point:
- Loads Decap CMS scripts
- Loads Netlify Identity widget for authentication

---

## Features Enabled

### ✅ Content Management
- Create, edit, delete posts
- Rich Markdown editor with toolbar
- Image uploads
- Category selection (dropdown)
- Date picker
- Gallery management (list of images)

### ✅ Local Development
- `local_backend: true` enables testing without Git
- Run `npm run cms` to start local backend on port 8081

### ✅ Editorial Workflow
- **Draft**: Work in progress posts
- **In Review**: Ready for review
- **Ready**: Approved and ready to publish
- All managed through Git branches

### ✅ Polish Language
- Interface translated to Polish
- Date format: DD.MM.YYYY
- Polish labels and hints

---

## Production Deployment

### Option 1: Netlify (Recommended)

#### Prerequisites
- Netlify account
- Repository connected to Netlify
- Site deployed

#### Steps

1. **Enable Netlify Identity:**
   - Go to Netlify Dashboard
   - Site Settings → Identity → Enable Identity

2. **Enable Git Gateway:**
   - Settings → Identity → Services → Git Gateway
   - Enable Git Gateway
   - Grant access to your repository

3. **Configure Registration:**
   - Settings → Identity → Registration
   - Set to "Invite only"

4. **Invite Users:**
   - Identity tab → Invite users
   - Send invitations to content editors
   - They'll receive email with setup link

5. **Update Config (if needed):**
   ```yaml
   backend:
     name: git-gateway
     branch: main
   ```

6. **Done!** Users can access `/admin/` and log in with their email.

---

### Option 2: GitHub OAuth (Self-hosted)

#### Prerequisites
- GitHub account with repo access
- OAuth app configured
- OAuth server (e.g., [netlify-cms-github-oauth-provider](https://github.com/vencax/netlify-cms-github-oauth-provider))

#### Steps

1. **Create GitHub OAuth App:**
   - GitHub → Settings → Developer settings → OAuth Apps
   - New OAuth App:
     - Name: `Hipoterapia CMS`
     - Homepage: `https://hipoterapia.bydgoszcz.pl`
     - Callback: `https://hipoterapia.bydgoszcz.pl/admin/`

2. **Save Credentials:**
   - Client ID
   - Client Secret

3. **Update Config:**
   ```yaml
   backend:
     name: github
     repo: username/repository-name
     branch: main
   ```

4. **Deploy OAuth Server:**
   - Deploy oauth provider with your credentials
   - Point CMS to your OAuth server endpoint

5. **Grant Access:**
   - Add collaborators to GitHub repo
   - They can now log in via GitHub

---

## Content Structure

### Aktualności (News Posts)

Location: `src/content/aktualnosci/`

**File Format:** MDX (Markdown + JSX)

**Frontmatter Schema:**
```yaml
---
title: "Post Title"                    # Required
pubDate: 2025-06-29                    # Required (YYYY-MM-DD)
description: "Short description"       # Optional
category: "biwaki-wycieczki"          # Required (select from dropdown)
gallery:                               # Optional (list of image paths)
  - "/uploads/folder/image1.webp"
  - "/uploads/folder/image2.webp"
---
```

**Categories:**
- `biwaki-wycieczki` - Biwaki i wycieczki
- `wydarzenia-sportowe` - Wydarzenia sportowe
- `zebrania-organizacyjne` - Zebrania i sprawy organizacyjne
- `wydarzenia-spoleczne` - Wydarzenia społeczne
- `programy-dotacyjne` - Programy dotacyjne

**Body Content:**
- Markdown formatting
- Can import Astro components
- Must include `<Gallery imagePaths={frontmatter.gallery} />` at end for gallery display

---

## File Uploads

### Image Uploads

**Destination:** `public/uploads/`
**Public Path:** `/uploads/`

**Supported Formats:**
- `.jpg`, `.jpeg`
- `.png`
- `.webp`
- `.gif`
- `.svg`

**Best Practices:**
- Compress images before upload (recommended max 2MB)
- Use WebP format for best performance
- Use descriptive filenames (e.g., `biwak-biskupin-01.webp`)
- Organize in folders by event/date

### Gallery Management

CMS stores gallery as YAML list:
```yaml
gallery:
  - "/uploads/event-name/photo1.webp"
  - "/uploads/event-name/photo2.webp"
```

Order in list = display order on site.

---

## Workflow

### Editorial Workflow

Enabled via `publish_mode: editorial_workflow`

**Three States:**

1. **Draft** (default)
   - New posts start here
   - Saved to `cms/draft` branch
   - Not published

2. **In Review**
   - Click "Set status → In Review"
   - Moved to `cms/pending_review` branch
   - Ready for review

3. **Ready / Published**
   - Click "Set status → Ready" or "Publish"
   - Merged to `main` branch
   - Live on site after build

### Direct Publish

If you don't want workflow:
```yaml
# Remove or comment out:
# publish_mode: editorial_workflow
```

All saves go directly to `main` branch.

---

## Customization

### Adding New Fields

Edit `public/admin/config.yml`:

```yaml
fields:
  - label: "New Field"
    name: "newField"
    widget: "string"  # or: text, number, boolean, select, etc.
    required: false
```

**Available Widgets:**
- `string` - Single line text
- `text` - Multi-line text
- `markdown` - Rich text editor
- `number` - Number input
- `boolean` - Checkbox
- `datetime` - Date/time picker
- `select` - Dropdown
- `list` - Repeating items
- `image` - Image upload
- `file` - File upload

### Adding New Collections

```yaml
collections:
  - name: "pages"
    label: "Strony"
    folder: "src/content/pages"
    create: true
    fields:
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Body", name: "body", widget: "markdown"}
```

---

## Troubleshooting

### CMS doesn't load

**Check:**
1. `/admin/` path is accessible
2. `public/admin/config.yml` exists
3. Console for JavaScript errors

**Fix:**
```bash
# Rebuild
npm run build

# Check for syntax errors in config.yml
```

### Can't authenticate (production)

**Check:**
1. Netlify Identity is enabled
2. Git Gateway is enabled
3. User has been invited
4. User confirmed email

### Local backend not working

**Check:**
1. `local_backend: true` in config.yml
2. `npm run cms` is running (port 8081)
3. Dev server is running

**Fix:**
```bash
# Terminal 1
npm run dev

# Terminal 2
npm run cms
```

### Changes not appearing on site

**Check:**
1. Post is published (not draft)
2. Site rebuilt after merge to main
3. Browser cache cleared

**Fix:**
```bash
# Manual rebuild
npm run build

# Clear cache
Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
```

### Gallery images not uploading

**Check:**
1. Image file size (< 5MB recommended)
2. Valid image format
3. Network connection

**Fix:**
- Compress image
- Try different browser
- Check browser console for errors

---

## Security Notes

### Production Checklist

- [ ] Set registration to "Invite only"
- [ ] Enable 2FA for admin accounts
- [ ] Only invite trusted users
- [ ] Regularly review user access
- [ ] Keep dependencies updated

### Access Control

**Netlify Identity:**
- Full access control via Netlify dashboard
- Can revoke user access anytime
- Email-based authentication

**GitHub OAuth:**
- Access tied to GitHub repo permissions
- Use teams for group access control
- Can revoke via GitHub settings

---

## Backup Strategy

### Automatic Backups

All content is stored in Git:
- Every change creates a commit
- Full history preserved
- Can revert any change

### Manual Backups

```bash
# Clone repository
git clone https://github.com/username/repo.git

# Or backup uploads folder
cp -r public/uploads /backup/location/
```

---

## Performance Tips

1. **Optimize Images:**
   - Use WebP format
   - Compress before upload
   - Max 1920px width recommended

2. **Content:**
   - Keep post length reasonable
   - Use pagination for long lists
   - Lazy load images in gallery

3. **Build:**
   - Astro generates static files
   - Fast page loads
   - No database queries

---

## Useful Links

- [Decap CMS Docs](https://decapcms.org/docs/)
- [Configuration Options](https://decapcms.org/docs/configuration-options/)
- [Widget Documentation](https://decapcms.org/docs/widgets/)
- [Netlify Identity](https://docs.netlify.com/security/secure-access-to-sites/identity/)
- [Markdown Guide](https://www.markdownguide.org/)

---

## Support

For technical support:
- Check [Decap CMS GitHub Issues](https://github.com/decaporg/decap-cms/issues)
- Review configuration documentation
- Test in local backend first

---

*Last updated: 2025-11-18*
