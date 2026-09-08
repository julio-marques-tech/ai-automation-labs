# Patient - FHIR v4.0.1

## Overview

The Patient resource documents "demographics and other administrative information about an individual or animal receiving care or other health-related services."

## Scope and Usage

This resource covers data about patients and animals involved in:
- Curative activities
- Psychiatric care
- Social services
- Pregnancy care
- Nursing and assisted living
- Dietary services
- Tracking of personal health and exercise data

The resource focuses on "who" information about the patient, emphasizing demographic data necessary for administrative, financial, and logistic procedures. Organizations maintain patient records, and individuals receiving care at multiple organizations may have multiple Patient Resources.

Concepts like race, ethnicity, organ donor status, and nationality exist in jurisdiction-specific profiles rather than the base resource.

## Resource Elements

### Core Elements

**identifier** (0..*)
- Type: Identifier
- Designation: An identifier for this patient

**active** (0..1)
- Type: boolean
- Designation: Whether this patient's record is in active use
- Note: Modifier element; systems use this to mark non-current patients

**name** (0..*)
- Type: HumanName
- Designation: A name associated with the patient

**telecom** (0..*)
- Type: ContactPoint
- Designation: A contact detail for the individual

**gender** (0..1)
- Type: code
- Values: male | female | other | unknown
- Binding: AdministrativeGender (Required)
- Designation: Administrative gender for record-keeping purposes

**birthDate** (0..1)
- Type: date
- Designation: The date of birth for the individual

**deceased[x]** (0..1)
- Type: deceasedBoolean or deceasedDateTime
- Designation: Indicates if the individual is deceased or not
- Note: Modifier element

**address** (0..*)
- Type: Address
- Designation: An address for the individual

**maritalStatus** (0..1)
- Type: CodeableConcept
- Binding: MaritalStatus (Extensible)
- Designation: Patient's most recent marital (civil) status

**multipleBirth[x]** (0..1)
- Type: multipleBirthBoolean or multipleBirthInteger
- Designation: Whether patient is part of a multiple birth

**photo** (0..*)
- Type: Attachment
- Designation: Image of the patient

### Contact Element

**contact** (0..*)
- Type: BackboneElement
- Designation: A contact party (e.g. guardian, partner, friend) for the patient
- Constraint: SHALL at least contain contact's details or reference to organization

**contact.relationship** (0..*)
- Type: CodeableConcept
- Binding: Patient Contact Relationship (Extensible)
- Designation: The kind of relationship

**contact.name** (0..1)
- Type: HumanName
- Designation: A name associated with the contact person

**contact.telecom** (0..*)
- Type: ContactPoint
- Designation: A contact detail for the person

**contact.address** (0..1)
- Type: Address
- Designation: Address for the contact person

**contact.gender** (0..1)
- Type: code
- Values: male | female | other | unknown
- Binding: AdministrativeGender (Required)

**contact.organization** (0..1)
- Type: Reference (Organization)
- Designation: Organization on behalf of which contact acts

**contact.period** (0..1)
- Type: Period
- Designation: Period during which contact is valid

### Communication Element

**communication** (0..*)
- Type: BackboneElement
- Designation: A language which may be used to communicate with the patient

**communication.language** (1..1)
- Type: CodeableConcept
- Binding: Common Languages (Preferred)
- Designation: The language which can be used to communicate about health

**communication.preferred** (0..1)
- Type: boolean
- Designation: Language preference indicator

### Clinical References

**generalPractitioner** (0..*)
- Type: Reference (Organization | Practitioner | PractitionerRole)
- Designation: Patient's nominated primary care provider

**managingOrganization** (0..1)
- Type: Reference (Organization)
- Designation: Organization that is the custodian of the patient record

### Linking Element

**link** (0..*)
- Type: BackboneElement
- Designation: Link to another patient resource that concerns the same actual person
- Note: Modifier element

**link.other** (1..1)
- Type: Reference (Patient | RelatedPerson)
- Designation: The other patient or related person resource that the link refers to

**link.type** (1..1)
- Type: code
- Values: replaced-by | replaces | refer | seealso
- Binding: LinkType (Required)
- Designation: The type of link between this patient resource and another

## References

The Patient resource is referenced by numerous clinical and administrative resources including Annotation, Account, AdverseEvent, AllergyIntolerance, Appointment, AuditEvent, CarePlan, Claim, Condition, Consent, Coverage, Device, Encounter, Flag, Goal, Immunization, MedicationRequest, Observation, Procedure, and others.

## Compartments

- Patient
- Practitioner
- RelatedPerson

Source: https://hl7.org/fhir/R4/patient.html
