# Onshoring Opportunity Matcher

Historical onshoring-opportunity project and supplier-data pipeline experiment.

## Current repository state

The current `main` branch does **not** contain the web matching application described by the original README.

The authoritative tree currently preserves one substantive implementation artifact:

- `My_workflow_2_Final_Updated (5).json` — an exported n8n workflow named **Onshoring Opportunity Match - Data Pipeline for USA Suppliers**.

That workflow is marked `"active": false` in the export. It defines a scheduled supplier-data collection pipeline that:

- fetches and parses supplier/source sitemaps from ThomasNet, IndustryNet, the SBA portal, and i5Services;
- extracts company, description, website, and source fields;
- merges the source streams;
- rate-limits selected requests; and
- upserts resulting supplier records into an Airtable `Suggestions` table.

The repository does not currently contain source code for the previously described browser UI that accepted a user's state, skills, and sector and returned personalized matches.

## Historical product direction

Earlier repository documentation described a web application intended to help entrepreneurs and workers discover U.S. onshoring opportunities by location, skills, and sector interests, including sectors such as semiconductors, clean energy, drones, and aerospace.

That product direction is preserved here as project history, but it should not be represented as current `main` implementation evidence.

The previously documented GitHub Pages URL was:

```text
https://JosephJMWalker-MBA.github.io/onshoring-opportunity-matcher
```

This cleanup review did not verify a current deployed application corresponding to the historical description.

## Current implementation boundary

What the repository demonstrates:

```text
public supplier/source pages
-> sitemap/page retrieval
-> HTML extraction
-> source tagging
-> merged supplier records
-> Airtable upsert
```

What it does **not** establish from current `main`:

- a live personalized opportunity-matching UI;
- validated matching quality;
- current market-size or federal-support recommendations;
- a user-feedback ingestion product;
- provenance-safe entity resolution across duplicate supplier names;
- a production deployment.

## Provenance caution

The workflow preserves a simple `source` label for extracted records, which is useful.

However, the final Airtable operation uses company name as the upsert key. If multiple source records share the same company name, downstream state can collapse distinct source observations unless the destination schema or execution environment preserves additional lineage outside this export.

The workflow export also contains a credential **reference name/id** for Airtable, not a secret token value. No live credential material should be added to the repository.

## Status

**Historical prototype / inactive workflow export.**

This repository is useful as evidence of an early supplier-data acquisition pipeline and as development provenance for later onshoring/opportunity work. It is not current evidence of a complete opportunity-matching product.

## Original intent

The project was created to support an Onshoring Initiative framework by making domestic manufacturing and employment opportunities easier to discover.

That intent remains part of the history even though the surviving implementation is narrower than the original product description.

## License

MIT License.
