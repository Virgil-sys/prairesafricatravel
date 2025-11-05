# Deploy Frontend and Backend to Netlify + Railway

## Tasks
- [x] Deploy backend to Render using existing render.yaml
- [x] Create render.yaml for frontend static site deployment
- [x] Update frontend JavaScript files to use the deployed backend URL
- [x] Fix render.yaml configuration issues (region, publishDir, staticSiteGenerator, plan, rootDir, buildCommand)
- [x] Deploy frontend to Render (Blueprint created, publishDir added)
- [x] Switch to Netlify + Railway (easier deployment)
- [x] Create netlify.toml for frontend deployment
- [x] Create railway.json for backend deployment
- [x] Update API_BASE_URL to Railway backend URL
- [x] Update CORS settings for Netlify domains
- [x] Add ignore rule to prevent Netlify rebuilds on backend changes
- [x] Remove old Vercel and Render config files to avoid confusion
- [x] Deploy frontend to Netlify (connect to GitHub repo)
- [x] Update all HTML files with Railway backend URL
- [ ] Deploy backend to Railway
- [ ] Test the full deployment

## Notes
- Switched from Render to Netlify + Railway for easier deployment
- Netlify handles static frontend with automatic deployments
- Railway provides simple Django deployment with database
- All configurations created and committed to GitHub
- Ready for deployment to both platforms
- Updated all HTML files (booking.html, booking-new.html, payment-status.html, upload-proof.html, test-api.html) with Railway backend URL
