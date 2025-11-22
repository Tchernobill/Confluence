

**Character Evolution Matrix**
```dataview
TABLE WITHOUT ID
	file.link as "Character",
	E.arc as "Tome",
	E.age as "Age",
	E.role as "Role",
	E.alignment as "Alignment",
	E.key_change as "Key Narrative Shift"
FROM #cast
FLATTEN evolution as E
SORT file.name ASC, E.arc ASC
```

**Alignement drift**
```dataview
TABLE WITHOUT ID
	file.link as "Name",
	map(evolution, (x) => "Tome " + x.arc + ": " + x.alignment) as "Moral Journey"
FROM #character
WHERE length(evolution) > 1
```
